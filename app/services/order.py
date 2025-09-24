from typing import Dict , List , Any

from app.core.enums.payment import PaymentType
from app.core.schemas.order import OrderResponse
from app.core.schemas.generic import MessageResponse
from app.core.exceptions import NotFoundException , InternalServerException
from app.infrastructures.repositories import MenuItemRepository , OrderRepository
from app.infrastructures.gateways.payment import EsewaGateway

class OrderService:
    """
        Service of order related usecases.
    """
    def __init__(
        self,
        order_repo: OrderRepository,
        menu_item_repo: MenuItemRepository
    ) -> None:
        self.menu_item_repo = menu_item_repo
        self.order_repo = order_repo
    
    async def create_order(self,type: PaymentType,data: List[Dict]):
        total: float = 0.0
        
        for item in data:
            menu_item = await self.menu_item_repo.retrieve_by_id(id=item["id"])
            if not menu_item:
                raise NotFoundException(message="Menu item not found.")
            total += item["quantity"] * menu_item.price
            
        try:
            instance = await self.order_repo.create(
                {
                    'amount':total,
                    'type':type.value,
                    'is_paid':False if type.value == "esewa" else True
                }
            )
            await self.order_repo.commit()
        except Exception as e:
            await self.order_repo.rollback()
            raise InternalServerException()
        
        return OrderResponse.model_validate(instance)
        
    async def retrieve_all(self) -> List[OrderResponse]:
        orders = await self.order_repo.retrieve_all()
        if not orders:
            raise NotFoundException(message="No orders found")
        return [
            OrderResponse.model_validate(order)
            for order in orders
        ]
    
    async def retrieve_by_id(self,id: str) -> OrderResponse:
        order = await self.order_repo.retrieve_by_id(id=id)
        if not order:
            raise NotFoundException(message="Order not found")
        return OrderResponse.model_validate(order)

    async def update_by_id(self,id: str,data: Dict[str,Any]) -> OrderResponse:
        order = await self.order_repo.retrieve_by_id(id=id)
        if not order:
            raise NotFoundException(message="Order not found")
        
        for key,value in data.items():
            if hasattr(order,key) and value is not None:
                setattr(order,key,value)
                
        try:
            await self.order_repo.update(order)
            await self.order_repo.commit()
        except Exception as e:
            await self.order_repo.rollback()
            raise InternalServerException()
        
        return OrderResponse.model_validate(order)
    
    async def delete_by_id(self,id: str) -> MessageResponse:
        try:
            order = await self.order_repo.retrieve_by_id(id=id)
            if not order:
                raise NotFoundException(message="Order not found")
            await self.order_repo.delete(instance=order)
            await self.order_repo.commit()
        except Exception as e:
            await self.order_repo.rollback()
            raise InternalServerException()
        return MessageResponse(message="Successfully deleted")