from sqlalchemy.orm import mapped_column, Mapped
from .base import Base

class CustomersORM(Base):
    username: Mapped[str]
    email: Mapped[str]
    city: Mapped[str]