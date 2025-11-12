from fastapi import Depends, HTTPException
from .repository import CustomersDAO
from typing import Annotated

async def get_customers_by_id(customer_id: int):
    result_query = await CustomersDAO().get_customers_by_id_dao(customer_id)
    if result_query:
        return result_query
    raise HTTPException(status_code=404, detail='Customer not found')
    

CustomersIdDep = Annotated[int, Depends(get_customers_by_id)]