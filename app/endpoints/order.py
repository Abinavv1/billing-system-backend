from typing import List

from fastapi import APIRouter , Depends
from dependency_injector.wiring import inject , Provide

from app.core.enums.payment import PaymentType
from app.container import Container
from app.core.schemas.generic import MessageResponse
from app.core.schemas.order import OrderProcessData , OrderResponse , OrderUpdate
from app.services import OrderService

router = APIRouter(prefix='/order',tags=['Order'])

@router.post('/')
@inject
async def create_order(
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
    return await service.create_order(type=type,data=data)

@router.get('/',response_model=List[OrderResponse])
@inject
async def retrieve_order_list(
    service: OrderService = Depends(Provide[Container.order_service])
):
    """
        Route to list all orders.
    """
    return await service.retrieve_all()

@router.get('/{id}',response_model=OrderResponse)
@inject
async def retrieve_order_by_id(
    id: str,
    service: OrderService = Depends(Provide[Container.order_service])
):
    """
        Route to retrieve a order by its ID.
    """
    return await service.retrieve_by_id(id=id)

@router.patch('/{id}',response_model=OrderResponse)
@inject
async def update_order_by_id(
    id: str,
    request: OrderUpdate,
    service: OrderService = Depends(Provide[Container.order_service])
):
    """
        Route to update a order by its ID.
    """
    return await service.update_by_id(id=id,data=request.model_dump())

@router.delete('/{id}',response_model=MessageResponse)
@inject
async def delete_order_by_id(
    id: str,
    service: OrderService = Depends(Provide[Container.order_service])
):
    """
        Route to delete a order by its ID.
    """
    return await service.delete_by_id(id=id)