from fastapi import FastAPI
from config import engine, session_factory, BASE_DIR
from sqlalchemy import text
import uvicorn

app = FastAPI()

@app.get("/version")
async def get_version_postgresql():
    version = None
    async with session_factory() as session:
        res = await session.execute(text("SELECT VERSION()"))
        version = res.scalar()
    return {"message": version}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)