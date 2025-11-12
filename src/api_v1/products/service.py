from .schemas import *
from .repository import ProductsDAO

class ProductsService:

    async def create_products_service(self, product: ProductPOSTSchemas):
        service = ProductsDAO()
        orm_model = await service.create_products_dao(product)
        dto_model = ProductGETSchemas.model_validate(orm_model, from_attributes=True) if orm_model else None
        return dto_model

    async def update_products_service(self, product_id: int, product: ProductPATCHSchemas):
        service = ProductsDAO()
        orm_model = await service.update_products_dao(product_id, product)
        dto_model = ProductGETSchemas.model_validate(orm_model, from_attributes=True) if orm_model else None
        return dto_model

    async def delete_products_service(self, product_id: int):
        service = ProductsDAO()
        await service.delete_products_dao(product_id)
        return None

    async def select_products_service(self):
        service = ProductsDAO()
        orm_model = await service.select_products_dao()
        dto_model = [ProductRelSchemas.model_validate(row, from_attributes=True) for row in orm_model] if orm_model else None
        return dto_model