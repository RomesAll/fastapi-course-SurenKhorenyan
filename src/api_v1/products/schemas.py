from pydantic import BaseModel, ConfigDict, EmailStr, Field
from config.models import ComplexityEnum
import datetime

class ProductPOSTSchemas(BaseModel):
    name: str
    desc: EmailStr
    duration_hours: int
    complexity: ComplexityEnum
    customer_id: int
    model_config = ConfigDict(from_attributes=True)

class ProductGETSchemas(ProductPOSTSchemas):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ProductPATCHSchemas(BaseModel):
    name: str | None = None
    desc: EmailStr | None = None
    duration_hours: str | None = None
    customer_id: int | None = None
    complexity: ComplexityEnum | None = None

from api_v1.customers.schemas import CustomerGETSchemas
class ProductRelSchemas(ProductGETSchemas):
    customer: "CustomerGETSchemas"