from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from .base import Base
import enum
from .customer import CustomersORM

class ComplexityEnum(enum.Enum):
    hard = "hard"
    easy = "easy"
    medium = "medium"

class ProductsORM(Base):
    name: Mapped[str]
    desc: Mapped[str] = mapped_column(default='...')
    duration_hours: Mapped[int]
    complexity: Mapped["ComplexityEnum"]
    customer_id: Mapped[int] = mapped_column(ForeignKey("customersorm.id", ondelete="CASCADE"))
    customer: Mapped["CustomersORM"] = relationship(back_populates="products")