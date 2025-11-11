from config import session_factory, CustomersORM
from .schemas import CustomerPOSTSchemas, CustomerOPTIONSSchemas
from typing import Optional
from sqlalchemy import select

class CustomersDAO:

    async def create_customers_dao(self, user: CustomerPOSTSchemas) -> Optional[int]:
        async with session_factory() as session:
            try:
                stmt = CustomersORM(**user.model_dump())
                session.add(stmt)
                await session.flush()
                await session.commit()
                return stmt.id
            except Exception as exc:
                return None

    async def update_customers_dao(customer: CustomersORM, customer_update: CustomerOPTIONSSchemas):
        async with session_factory() as session:
            try:
                for name, value in customer_update.model_dump(exclude_unset=True).items():
                    setattr(customer, name, value)
                await session.commit()
                return customer
            except Exception as exc:
                return None

    async def delete_customers_dao():
        async with session_factory() as session:
            session.delete(CustomersORM)
            await session.commit()

    async def select_customers_dao():
        async with session_factory() as session:
            try:
                stmt = select(CustomersORM)
                result = await session.execute(stmt)
                return result
            except Exception as exc:
                return None
