from config import session_factory
from config.models import CustomersORM
from .schemas import CustomerPOSTSchemas, CustomerPATCHSchemas
from typing import Optional
from sqlalchemy import select

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
                for name, value in customer_update.model_dump(exclude_unset=True).items():
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
                stmt = select(CustomersORM)
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