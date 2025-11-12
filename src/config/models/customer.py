from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import Base

class CustomersORM(Base):
    username: Mapped[str]
    email: Mapped[str]
    city: Mapped[str]
    products: Mapped[list["ProductsORM"]] = relationship(back_populates="customer")