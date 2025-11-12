from .repository import *
from .schemas import *
from fastapi import APIRouter, HTTPException, Depends
from .service import *
from .depends import CustomersIdDep, get_customers_by_id

router = APIRouter()

@router.get('/all')
async def select_customers():
    result = await CustomersService().select_customers_service()
    if result:
        return result
    raise HTTPException(status_code=400, detail='')

@router.post('/create')
async def create_customers(customer: CustomerPOSTSchemas):
    result = await CustomersService().create_customers_service(customer)
    if result:
        return result
    raise HTTPException(status_code=400, detail='')

@router.patch('/update')
async def update_customers(customer_id: CustomersIdDep, customer_info: CustomerPATCHSchemas):
    result = await CustomersService().update_customers_service(customer_id, customer_info)
    if result:
        return result
    raise HTTPException(status_code=400, detail='Bad request')

@router.delete('/delete')
async def delete_customers(customer_id: CustomersIdDep):
    await CustomersService().delete_customers_service(customer_id)
    return {"message": f"User {customer_id} has been deleted"}