from typing import List

from fastapi import APIRouter , Depends
from dependency_injector.wiring import inject , Provide

from app.core.enums.payment import PaymentType
from app.container import Container
from app.core.schemas.order import OrderProcessData
from app.services import OrderService

router = APIRouter(prefix='/order',tags=['Order'])

@router.post('/process/')
@inject
async def process_order(
    type: PaymentType,
    request: List[OrderProcessData],
    service: OrderService = Depends(Provide[Container.order_service])
):
    """
        Route to process order.
    """
    data = [
        item.model_dump()
        for item in request
    ]
    return await service.process_order(type=type,data=data)