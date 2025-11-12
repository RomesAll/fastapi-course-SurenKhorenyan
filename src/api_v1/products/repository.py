from config import session_factory
from config.models import ProductsORM
from .schemas import ProductPOSTSchemas, ProductPATCHSchemas, ProductRelSchemas
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from config.models import CustomersORM

class ProductsDAO:

    async def create_products_dao(self, product: ProductPOSTSchemas) -> Optional[ProductsORM]:
        async with session_factory() as session:
            try:
                stmt = ProductsORM(**product.model_dump())
                session.add(stmt)
                await session.flush()
                await session.commit()
                return stmt
            except Exception as exc:
                return None

    async def update_products_dao(self, product_id: int, product_update: ProductPATCHSchemas) -> Optional[ProductsORM]:
        async with session_factory() as session:
            try:
                product = await session.get(ProductsORM, product_id)
                product_new_info = product_update.model_dump(exclude_none=True).items()
                if not product_new_info:
                    return product
                for name, value in product_new_info:
                    setattr(product, name, value)
                await session.commit()
                return product
            except Exception as exc:
                return None

    async def delete_products_dao(self, product_id: int) -> None:
        async with session_factory() as session:
            product = await session.get(ProductsORM, product_id)
            await session.delete(product)
            await session.commit()

    async def select_products_dao(self) -> list[ProductsORM]:
        async with session_factory() as session:
            try:
                stmt = select(ProductsORM).options(joinedload(CustomersORM.products))
                result = await session.execute(stmt)
                return result.scalars().all()
            except Exception as exc:
                return None
            
    async def get_products_by_id_dao(self, product_id: int) -> ProductsORM:
        async with session_factory() as session:
            try:
                product = await session.get(ProductsORM, product_id)
                if product.id:
                    return product.id
            except:
                return None