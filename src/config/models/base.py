from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy import MetaData, text
import datetime

class Base(DeclarativeBase):

    metadata = MetaData()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        attrs = []
        for ind, col in enumerate(self.__table__.columns.keys()):
            attrs.append(f"{col}={getattr(self, col)}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"