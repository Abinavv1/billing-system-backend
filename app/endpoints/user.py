from typing import List , Dict , Any

from fastapi import APIRouter , Depends
from dependency_injector.wiring import inject , Provide

from app.container import Container
from app.services import UserService
from app.dependencies.token import get_admin
from app.core.schemas.generic import MessageResponse
from app.core.schemas.user import UserResponse , UserRegister , UserUpdate

router = APIRouter(prefix='/user',tags=['User'],dependencies=[Depends(get_admin)])

@router.post('/register')
@inject
async def register_user(
    request: UserRegister,
    service: UserService = Depends(Provide[Container.user_service])
):
    """
        Route to register new user.
    """
    return await service.register_user(data=request.model_dump())
    
@router.get('/',response_model=List[UserResponse])
@inject
async def retrieve_users_list(
    service: UserService = Depends(Provide[Container.user_service])
):
    """
        Route to list all users.
    """
    return await service.retrieve_all()

@router.get('/{id}',response_model=UserResponse)
@inject
async def retrieve_user_by_id(
    id: str,
    service: UserService = Depends(Provide[Container.user_service])
):
    """
        Route to retrieve user by its ID.
    """
    return await service.retrieve_by_id(id=id)

@router.patch('/{id}',response_model=UserResponse)
@inject
async def update_user_by_id(
    id: str,
    request: UserUpdate,
    service: UserService = Depends(Provide[Container.user_service])
):
    """
        Route to update existing user by its ID.
    """
    return await service.update_by_id(id=id,data=request.model_dump())

@router.delete('/{id}',response_model=MessageResponse)
@inject
async def delete_user_by_id(
    id: str,
    service: UserService = Depends(Provide[Container.user_service])
):
    """
        Route to delete a user by its ID.
    """
    return await service.delete_by_id(id=id)