from pydantic import BaseModel, ConfigDict, EmailStr, Field

class CustomerPOSTSchemas(BaseModel):
    username: str
    email: EmailStr
    city: str
    model_config = ConfigDict(from_attributes=True)

class CustomerGETSchemas(CustomerPOSTSchemas):
    id: int

class CustomerOPTIONSSchemas(CustomerPOSTSchemas):
    username: str | None = None
    email: EmailStr | None = None
    city: str | None = None