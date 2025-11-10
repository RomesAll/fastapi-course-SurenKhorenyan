from pydantic import BaseModel, ConfigDict, EmailStr, Field

class CustomerAddSchemas(BaseModel):
    username: str
    email: EmailStr
    city: str
    model_config = ConfigDict(from_attributes=True)

class CustomerUpdateSchemas(CustomerAddSchemas):
    id: int