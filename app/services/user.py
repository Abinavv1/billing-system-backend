from typing import Dict , Any , List

from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import ConflictException , InternalServerException , NotFoundException
from app.core.schemas.user import UserResponse
from app.core.schemas.generic import MessageResponse
from app.infrastructures.repositories import UserRepository
from app.infrastructures.utils.hasher import generate_hash

class UserService:
    """
        Service for user related service.
    """
    def __init__(
        self,
        user_repo: UserRepository
    ) -> None:
        self.user_repo = user_repo
    
    async def register_user(self,data: Dict[str,Any]) -> UserResponse:
        if await self.user_repo.retrieve_by_email(email=data['email']):
            raise ConflictException(message="Email already taken.")
        
        data["password"] = await generate_hash(value=data["password"])

        try:
            user = await self.user_repo.create(data=data)
            await self.user_repo.commit()         
        except SQLAlchemyError as e:
            await self.user_repo.rollback()   
            raise InternalServerException() 
        
        return UserResponse.model_validate(user)

    async def retrieve_all(self) -> List[UserResponse]:
        users = await self.user_repo.retrieve_all()
        if not users:
            raise NotFoundException(message="No users found")
        
        return [
            UserResponse.model_validate(user)
            for user in users
        ]
        
    async def retrieve_by_id(self,id: str) -> UserResponse:
        user = await self.user_repo.retrieve_by_id(id=id)
        if not user:
            raise NotFoundException(message="User not found")
        return UserResponse.model_validate(user)
    
    async def update_by_id(self,id: str,data: Dict[str,Any]) -> UserResponse:
        user = await self.user_repo.retrieve_by_id(id=id)
        if not user:
            raise NotFoundException(message="User not found")
        
        if ( 
            "email" in data
            and data["email"] is not None
            and data["email"] != user.email
            and await self.user_repo.retrieve_by_email(email=data["email"])
        ):
            raise ConflictException(message="Email already taken.")
        
        for key,value in data.items():
            if hasattr(user,key) and value is not None:
                setattr(user,key,value)
        try:
            updated = await self.user_repo.update(updated=user)
            await self.user_repo.commit()
        except SQLAlchemyError:
            await self.user_repo.rollback()
            raise InternalServerException()
        
        return UserResponse.model_validate(updated)
    
    async def delete_by_id(self,id: str) -> MessageResponse:
        user = await self.user_repo.retrieve_by_id(id=id)
        if not user:
            raise NotFoundException(message="User not found")
        
        try:
            await self.user_repo.delete(instance=user)
            await self.user_repo.commit()
            return MessageResponse(message="Successfully deleted")       
        except SQLAlchemyError as e:
            print(e)
            await self.user_repo.rollback()
            raise InternalServerException()
        
        