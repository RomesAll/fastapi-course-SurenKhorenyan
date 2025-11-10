from sqlalchemy.orm import mapped_column, Mapped
from .base import Base
import enum

class ComplexityEnum(enum.Enum):
    hard = "hard"
    easy = "easy"
    medium = "medium"

class ProductsORM(Base):
    name: Mapped[str]
    desc: Mapped[str] = mapped_column(default='...')
    duration_hours: Mapped[int]
    complexity: Mapped["ComplexityEnum"]