from fastapi import FastAPI, Depends, HTTPException, status, Header, Request
import uvicorn, secrets
from typing import Annotated
from fastapi.security import HTTPBasicCredentials, HTTPBasic

app = FastAPI()
''' Basic auth
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

''' Token basic auth
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
    return {"message": f"Hello - {username}"}
'''


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)