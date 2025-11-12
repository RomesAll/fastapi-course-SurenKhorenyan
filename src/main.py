from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import session_factory
from sqlalchemy import text
from api_v1 import router
import uvicorn

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     pass
    # async with engine.begin() as conn:
    #     # await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)
    # yield
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)

app = FastAPI()
app.include_router(router)

@app.get("/version")
async def get_version_postgresql():
    async with session_factory() as session:
        res = await session.execute(text("SELECT VERSION()"))
        res_scalar = res.scalar()
    return {"message": res_scalar}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)