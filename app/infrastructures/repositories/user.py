from typing import Optional

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructures.models import User
from app.infrastructures.repositories.base import Repository

class UserRepository(Repository[User]):
    """
        Repository for `User` model.
    """
    def __init__(self,session: AsyncSession) -> None:
        super().__init__(session=session,model=User)
    
    async def retrieve_by_email(self,email: str) -> Optional[User]:
        """
            Retrieve model instance by its email.
        """
        result = await self._session.execute(select(self._model).where(self._model.email == email))
        return result.scalar_one_or_none()
        