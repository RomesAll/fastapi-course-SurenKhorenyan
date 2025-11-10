from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

class Base(DeclarativeBase):

    metadata = MetaData()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    # def __repr__(self):
    #     self.__table__.columns.keys()
    #     return super().__repr__()