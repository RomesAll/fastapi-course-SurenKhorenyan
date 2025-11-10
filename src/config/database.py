from .project_config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(url=settings.DATABASE_URL_async, echo=True)
session_factory = async_sessionmaker(bind=engine)