from .repository import *
from .schemas import *
from fastapi import APIRouter, HTTPException
from .service import *
from .depends import ProductsIdDep, ProductsInfoDep

router = APIRouter()

@router.get('/all')
async def select_products():
    result = await ProductsService().select_products_service()
    if result:
        return result
    raise HTTPException(status_code=400, detail='Bad request')

@router.post('/create')
async def create_products(product: ProductPOSTSchemas):
    result = await ProductsService().create_products_service(product)
    if result:
        return result
    raise HTTPException(status_code=400, detail='Bad request')

@router.patch('/update')
async def update_products(product_id: ProductsIdDep, product_info: ProductsInfoDep):
    result = await ProductsService().update_products_service(product_id, product_info)
    if result:
        return result
    raise HTTPException(status_code=400, detail='Bad request')

@router.delete('/delete')
async def delete_products(product_id: ProductsIdDep):
    await ProductsService().delete_products_service(product_id)
    return {"message": f"Product {product_id} has been deleted"}