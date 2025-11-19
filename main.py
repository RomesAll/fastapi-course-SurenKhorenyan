import uuid
from fastapi import FastAPI, Depends, HTTPException, status, Header, Request, Cookie, Response
import uvicorn, secrets, bcrypt, jwt
from typing import Annotated
from fastapi.security import HTTPBasicCredentials, HTTPBasic, HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, ConfigDict
from pathlib import Path
from pydantic import SecretStr
from datetime import datetime, timedelta

#secrets.compare_digest() и SecretStr(pydantic) Не полноценный вариант, лучше использовать bcrypt

app = FastAPI()

'''# Basic auth
security = HTTPBasic()
user_db = {
    'admin': '123',
    'roman': 'qwerty',
}
def get_user_info(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    exception_401 = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    user_password = user_db.get(credentials.username, None)
    if not user_password:
        raise exception_401
    if not secrets.compare_digest(credentials.password, user_password):
        raise exception_401
    return credentials.username

@app.get('/auth')
def demo_auth_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {'message': 'Hi', 'username': credentials.username}

@app.get('/auth/userinfo')
def demo_auth_get_user_info(username: str = Depends(get_user_info)):
    return {'message': f'Hello {username}'}'''

'''# Token basic auth
user_info = {
    '66d5f2222990e2a42a796277372ccbb12284aa9af5dc9233101e6818187d37d0': 'amdin',
    '064dafd23cac1b9fd7db239b1a83657b13410938c0d1bcdd7f552b3089041bce': 'roman'
}

def get_user_info(request: Request, token = Header(alias='x-auth-token')):
    username = user_info.get(token, None)
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    return username

@app.get('/auth/token')
def get_username(username = Depends(get_user_info)):
    return {"message": f"Hello - {username}"}'''

'''# Cookies auth
COOKIES_NAME = 'session-id-cookie'
cookies_user_info = {
    'qwerty123': {
        'username': 'roman',
        'password': '123'
    }, 
}

def get_user_by_session(session_id: str | None = Cookie(alias=COOKIES_NAME, default=None)):
    if not session_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Session is not valid')
    return cookies_user_info.get(session_id, None)

@app.post('/login/cookies')
def login(response: Response, session_id: str):
    user_info = cookies_user_info.get(session_id, None)
    if user_info is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    response.set_cookie(COOKIES_NAME, session_id)
    return {'message': 'ok'}

@app.post('/logout')
def logout(response: Response):
    response.delete_cookie(COOKIES_NAME)
    return {'message': 'ok'}

@app.get('/user/info')
def get_user_info(user_info = Depends(get_user_by_session)):
    if user_info is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user_info'''

# JWT Token

BASE_DIR = Path(__file__).parent

class AuthJWT(BaseModel):
    public_key_path: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    private_key_path: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    algoritm: str = 'RS256'
    access_token_exp: int = 10

class UserSchema(BaseModel):
    username: str
    password: bytes
    active: bool = True
    model_config = ConfigDict(strict=True)

class TokenInfo(BaseModel):
    access_token: str
    token_type: str

class UserCreds(BaseModel):
    username: str
    password: str

auth_jwt = AuthJWT()

def encode_jwt(payload: dict, 
               pivate_key=auth_jwt.private_key_path.read_text(), 
               algorithm=auth_jwt.algoritm,
               exp=auth_jwt.access_token_exp):
    update_payload = payload.copy()
    update_payload['exp'] = datetime.utcnow() + timedelta(minutes=exp)
    update_payload['iat'] = datetime.utcnow()
    encoded_token = jwt.encode(payload=update_payload, key=pivate_key, algorithm=algorithm)
    return encoded_token

def decode_jwt(token, 
               public_key=auth_jwt.public_key_path.read_text(), 
               algorithm=auth_jwt.algoritm):
    decoded_token = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded_token

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(password=pwd_bytes, salt=salt)

def check_validate_password(password: str, hashed_password: bytes) ->bool:
    return bcrypt.checkpw(password.encode(), hashed_password)

user_1 = UserSchema(username='roman', password=hash_password('qwerty'), active=True)
user_2 = UserSchema(username='josh', password=hash_password('1111'), active=True)

user_db = {
    user_1.username: user_1,
    user_2.username: user_2
}

def validate_user_info(creds: UserCreds = Depends(UserCreds)):
    if not creds.username in user_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    psw_hashed = hash_password(creds.password)
    if not check_validate_password(creds.password, psw_hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user_db.get(creds.username)

@app.post('/login')
def login(response: Response, user: UserSchema = Depends(validate_user_info)):
    payload = {
        "sub": user.username,
        "username": user.username
    }
    token = encode_jwt(payload)
    response.set_cookie('Authorization', f'Bearer {token}')
    return TokenInfo(access_token=token, token_type='Bearer')

def validate_token(token: str | None = Cookie(alias='Authorization', default=None)):
    if token is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid token')
    token_type, access_token = token.split(' ')
    payload = decode_jwt(access_token)
    return payload

@app.get('/user/info')
def get_user_info(user_info = Depends(validate_token)):
    return {"message": user_info.get('sub')}

@app.post('/logout')
def logout(resonse: Response):
    resonse.delete_cookie('Authorization')
    return {'message': 'ok'}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)