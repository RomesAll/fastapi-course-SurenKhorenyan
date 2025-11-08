from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn

app = FastAPI()

class UserSchemas(BaseModel):
    email: EmailStr

@app.get("/")
def index():
    return {"message": "hello index"}

@app.get("/item/{id}")
def item(id: int):
    return {"message": id}

@app.post("/item")
def get_message(message: str = Body()):
    return {"message": f"hello {message}"}

@app.post('/users')
def create_users(user: UserSchemas):
    return {"message": user.email}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)