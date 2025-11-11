from config import session_factory, CustomersORM
from .schemas import *
from .repository import CustomersDAO

class CustomersService:

    async def create_customers_service(customer: CustomerPOSTSchemas):
        service = CustomersDAO()
        orm_model = await service.create_customers_dao(customer)
        dto_model = CustomerGETSchemas.from_orm(orm_model) if orm_model else None
        return dto_model

    async def update_customers_service(customer: CustomerOPTIONSSchemas):
        service = CustomersDAO()
        orm_model = await service.update_customers_dao(CustomersORM(), customer)
        dto_model = CustomerGETSchemas.model_validate(orm_model, from_attributes=True) if orm_model else None
        return dto_model

    async def delete_customers_service(customer_id: int):
        service = CustomersDAO()
        await service.delete_customers_dao(customer_id)
        return None

    async def select_customers_service():
        service = CustomersDAO()
        orm_model = await service.select_customers_dao()
        dto_model = [CustomerGETSchemas.model_validate(row, from_attributes=True) for row in orm_model] if orm_model else None
        return dto_model
        
