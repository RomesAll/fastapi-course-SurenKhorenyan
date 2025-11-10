from .repository import CustomersDAO
from .schemas import CustomerAddSchemas
from fastapi import APIRouter

router = APIRouter()

@router.post('/create')
async def create_customers(user: CustomerAddSchemas):
    new_user = CustomersDAO()
    res = await new_user.create_customers_dao(user)