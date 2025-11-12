from .schemas import *
from .repository import CustomersDAO

class CustomersService:

    async def create_customers_service(self, customer: CustomerPOSTSchemas):
        service = CustomersDAO()
        orm_model = await service.create_customers_dao(customer)
        dto_model = CustomerGETSchemas.model_validate(orm_model, from_attributes=True) if orm_model else None
        return dto_model

    async def update_customers_service(self, customer_id: int, customer: CustomerPATCHSchemas):
        service = CustomersDAO()
        orm_model = await service.update_customers_dao(customer_id, customer)
        dto_model = CustomerGETSchemas.model_validate(orm_model, from_attributes=True) if orm_model else None
        return dto_model

    async def delete_customers_service(self, customer_id: int):
        service = CustomersDAO()
        await service.delete_customers_dao(customer_id)
        return None

    async def select_customers_service(self):
        service = CustomersDAO()
        orm_model = await service.select_customers_dao()
        dto_model = [CustomerRelSchemas.model_validate(row, from_attributes=True) for row in orm_model] if orm_model else None
        return dto_model