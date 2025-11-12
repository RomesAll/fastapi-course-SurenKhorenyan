from pydantic import BaseModel, ConfigDict, EmailStr, Field
import datetime

class CustomerPOSTSchemas(BaseModel):
    username: str
    email: EmailStr
    city: str
    model_config = ConfigDict(from_attributes=True)

class CustomerGETSchemas(CustomerPOSTSchemas):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CustomerPATCHSchemas(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    city: str | None = None

from api_v1.products.schemas import ProductGETSchemas
class CustomerRelSchemas(CustomerGETSchemas):
    products: list["ProductGETSchemas"]