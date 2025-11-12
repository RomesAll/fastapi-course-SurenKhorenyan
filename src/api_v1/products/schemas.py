from pydantic import BaseModel, ConfigDict, EmailStr, Field
from config.models import ComplexityEnum

class ProductPOSTSchemas(BaseModel):
    name: str
    desc: EmailStr
    duration_hours: int
    complexity: ComplexityEnum
    model_config = ConfigDict(from_attributes=True)

class ProductGETSchemas(ProductPOSTSchemas):
    id: int

class ProductPATCHSchemas(BaseModel):
    name: str | None = None
    desc: EmailStr | None = None
    duration_hours: str | None = None
    complexity: ComplexityEnum | None = None

class ProductRelSchemas(ProductGETSchemas):
    customer: "CustomersORM"