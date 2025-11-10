from fastapi import APIRouter
from .customers.views import router as customer_router
# from .products.views import router as products_router

router = APIRouter(prefix="/customer")
router.include_router(customer_router)
# router.include_router(products_router)