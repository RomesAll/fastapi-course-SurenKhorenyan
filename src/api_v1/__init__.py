from fastapi import APIRouter
from .customers.views import router as customer_router

router = APIRouter(prefix="/customer", tags=["Customer"])
router.include_router(customer_router)