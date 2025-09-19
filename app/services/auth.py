from typing import Dict , Any

from app.core.exceptions import LoginException
from app.core.schemas.token import TokenResponse
from app.infrastructures.repositories import UserRepository
from app.infrastructures.utils.hasher import verify_hash
from app.infrastructures.utils.token import generate_token

class AuthService:
    """
        Service for auth related operations.
    """
    def __init__(
        self,
        user_repo: UserRepository
    ) -> None:
        self.user_repo = user_repo
    
    async def validate_login(self,data: Dict[str,Any]) -> TokenResponse:
        user = await self.user_repo.retrieve_by_email(email=data["email"])
        if not user:
            raise LoginException(message="Invalid email or password")
        if not await verify_hash(data["password"],user.password):
            raise LoginException(message="Invalid email or password")
        
        token = await generate_token(payload={
            "id":user.id,
            "role":"admin" if user.is_admin else "user"
        })
        
        return TokenResponse(token=token)