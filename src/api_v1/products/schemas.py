from pydantic import BaseModel, ConfigDict, EmailStr, Field

class ProductPOSTSchemas(BaseModel):
    name: str
    desc: EmailStr
    duration_hours: str
    complexity: str
    model_config = ConfigDict(from_attributes=True)

class ProductGETSchemas(ProductPOSTSchemas):
    id: int

class ProductPATCHSchemas(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    city: str | None = None