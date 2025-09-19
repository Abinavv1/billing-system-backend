from typing import Dict , Any , List , Optional

from app.core.schemas.menu_item import MenuItemResponse
from app.core.schemas.generic import MessageResponse
from app.core.exceptions import ConflictException , InternalServerException , NotFoundException
from app.infrastructures.repositories import MenuItemRepository

class MenuItemService:
    def __init__(
        self,
        menu_item_repo: MenuItemRepository
    ) -> None:
        self.menu_item_repo = menu_item_repo
        
    async def create_menu_item(self,data: Dict[str,Any]) -> MenuItemResponse:
        if await self.menu_item_repo.retrieve_by_name(item_name=data["item_name"]):
            raise ConflictException(message="Item already exists.")

        try:
            menu_item = await self.menu_item_repo.create(data=data)
            await self.menu_item_repo.commit()
        except Exception as e:
            print(e)
            await self.menu_item_repo.rollback()
            raise InternalServerException()
        
        return MenuItemResponse.model_validate(menu_item)
    
    async def retrieve_all(self) -> List[MenuItemResponse]:
        items = await self.menu_item_repo.retrieve_all()
        if not items:
            raise NotFoundException(message="No items found.")
        return [
            MenuItemResponse.model_validate(item)
            for item in items
        ]
    
    async def retrieve_by_id(self,id: str) -> Optional[MenuItemResponse]:
        item = await self.menu_item_repo.retrieve_by_id(id=id)
        if not item:
            raise NotFoundException(message="Menu item not found.")
        return MenuItemResponse.model_validate(item)
    
    async def update_by_id(self,id: str,data: Dict[str,Any]) -> MenuItemResponse:
        item = await self.menu_item_repo.retrieve_by_id(id=id)
        if not item:
            raise NotFoundException(message="Menu item not found.")
        
        if (
            "item_name" in data
            and data["item_name"] is not None
            and await self.menu_item_repo.retrieve_by_name(item_name=data["item_name"])
        ):
            raise ConflictException(message="Item already exists.")
        
        for key,value in data.items():
            if hasattr(item,key) and value is not None:
                setattr(item,key,value)
        
        try:
            updated = await self.menu_item_repo.update(item)
            await self.menu_item_repo.commit()
        except Exception as e:
            print(e)
            await self.menu_item_repo.rollback()
            raise InternalServerException()
            
        return MenuItemResponse.model_validate(updated)
    
    async def delete_by_id(self,id: str) -> MessageResponse:
        item = await self.menu_item_repo.retrieve_by_id(id=id)
        if not item:
            raise NotFoundException(message="Menu item not found.")
        
        try:
            await self.menu_item_repo.delete(item)
            await self.menu_item_repo.commit()
        except Exception as e:
            await self.menu_item_repo.rollback()
            raise InternalServerException()
        
        return MessageResponse(message="Menu item successfully deleted.")
            