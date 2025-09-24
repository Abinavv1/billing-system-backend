from fastapi import APIRouter

from .auth import router as auth_router
from .user import router as user_router
from .menu_item import router as menu_item_router
from .order import router as order_router
from .payment import router as payment_router

router = APIRouter(prefix='/api')
router.include_router(router=auth_router)
router.include_router(router=user_router)
router.include_router(router=menu_item_router)
router.include_router(router=order_router)
router.include_router(router=payment_router)

