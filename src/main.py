from fastapi import FastAPI
from config import engine, session_factory, BASE_DIR, ProductsORM, CustomersORM, ComplexityEnum, Base
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

@app.post("/setupdb")
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        pr = CustomersORM(username='asd', email='sdf', city='sdf')
        print(pr)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)