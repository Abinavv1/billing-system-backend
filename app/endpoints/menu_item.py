from typing import List

from fastapi import APIRouter , Depends
from dependency_injector.wiring import inject , Provide

from app.container import Container
from app.dependencies.token import get_admin
from app.core.schemas.generic import MessageResponse
from app.core.schemas.menu_item import MenuItemCreate , MenuItemUpdate , MenuItemResponse
from app.services import MenuItemService

router = APIRouter(prefix='/menu-item',tags=["Menu-item"])

@router.post('/',dependencies=[Depends(get_admin)],response_model=MenuItemResponse)
@inject
async def create_menu_item(
    request: MenuItemCreate,
    service: MenuItemService = Depends(Provide[Container.menu_item_service])
):
    """
        Route to create new menu item
    """
    return await service.create_menu_item(data=request.model_dump())

@router.get('/',response_model=List[MenuItemResponse])
@inject
async def retrieve_all_menu_item(
    service: MenuItemService = Depends(Provide[Container.menu_item_service])
):
    """
        Route to retrieve all menu items.
    """
    return await service.retrieve_all()

@router.get('/{id}',response_model=MenuItemResponse)
@inject
async def retrieve_menu_item_by_id(
    id: str,
    service: MenuItemService = Depends(Provide[Container.menu_item_service])
):
    """
        Route to retrive menu item by its ID.
    """
    return await service.retrieve_by_id(id=id)

@router.patch('/{id}',dependencies=[Depends(get_admin)],response_model=MenuItemResponse)
@inject
async def update_menu_item_by_id(
    id: str,
    request: MenuItemUpdate,
    service: MenuItemService = Depends(Provide[Container.menu_item_service])
):
    """
        Route to update menu itme by its ID.
    """
    return await service.update_by_id(id=id,data=request.model_dump())

@router.delete('/{id}',dependencies=[Depends(get_admin)],response_model=MessageResponse)
@inject
async def delete_menu_item_by_id(
    id: str,
    service: MenuItemService = Depends(Provide[Container.menu_item_service])
):
    """
        Route to delete menu item by its ID.
    """
    return await service.delete_by_id(id=id)