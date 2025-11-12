from fastapi import Depends, HTTPException
from typing import Annotated
from .schemas import ProductPATCHSchemas
from .service import ProductsDAO

async def get_product_by_id(product_id: int):
    result_query = await ProductsDAO().get_products_by_id_dao(product_id)
    if result_query:
        return result_query
    raise HTTPException(status_code=404, detail='Product not found')   

ProductsIdDep = Annotated[int, Depends(get_product_by_id)]
ProductsInfoDep = Annotated[ProductPATCHSchemas, Depends(ProductPATCHSchemas)]