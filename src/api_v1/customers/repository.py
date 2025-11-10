from config import session_factory, CustomersORM
from .schemas import CustomerAddSchemas
from typing import Optional
from sqlalchemy import select

class CustomersDAO:

    async def create_customers_dao(self, user: CustomerAddSchemas) -> Optional[int]:
        async with session_factory() as session:
            try:
                stmt = CustomersORM(**user.model_dump())
                session.add(stmt)
                await session.flush()
                await session.commit()
                return stmt.id
            except Exception as exc:
                return None

    async def update_customers_dao():
        pass

    async def delete_customers_dao():
        pass

    async def select_customers_dao():
        pass