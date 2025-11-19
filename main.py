from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn, secrets
from typing import Annotated
from fastapi.security import HTTPBasicCredentials, HTTPBasic

app = FastAPI()
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
    return {'message': f'Hello {username}'}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)