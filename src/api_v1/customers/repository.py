from config import session_factory
from config.models import CustomersORM
from .schemas import CustomerPOSTSchemas, CustomerPATCHSchemas
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from config.models import ProductsORM

class CustomersDAO:

    async def create_customers_dao(self, customer: CustomerPOSTSchemas) -> Optional[CustomersORM]:
        async with session_factory() as session:
            try:
                stmt = CustomersORM(**customer.model_dump())
                session.add(stmt)
                await session.flush()
                await session.commit()
                return stmt
            except Exception as exc:
                return None

    async def update_customers_dao(self, customer_id: int, customer_update: CustomerPATCHSchemas) -> Optional[CustomersORM]:
        async with session_factory() as session:
            try:
                customer = await session.get(CustomersORM, customer_id)
                customer_new_info = customer_update.model_dump(exclude_none=True).items()
                if not customer_new_info:
                    return customer
                for name, value in customer_new_info:
                    setattr(customer, name, value)
                await session.commit()
                return customer
            except Exception as exc:
                return None

    async def delete_customers_dao(self, customer_id: int) -> None:
        async with session_factory() as session:
            customer = await session.get(CustomersORM, customer_id)
            await session.delete(customer)
            await session.commit()

    async def select_customers_dao(self) -> list[CustomersORM]:
        async with session_factory() as session:
            try:
                stmt = select(CustomersORM).options(selectinload(ProductsORM))
                result = await session.execute(stmt)
                return result.scalars().all()
            except Exception as exc:
                return None
            
    async def get_customers_by_id_dao(self, customer_id: int) -> CustomersORM:
        async with session_factory() as session:
            try:
                customer = await session.get(CustomersORM, customer_id)
                if customer.id:
                    return customer.id
            except:
                return None