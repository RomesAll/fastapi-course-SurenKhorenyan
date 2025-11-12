from fastapi import APIRouter
from .customers.views import router as customer_router
from .products.views import router as product_router

router = APIRouter()
router.include_router(customer_router)
router.include_router(product_router)