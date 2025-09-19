from typing import Optional

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructures.models import MenuItem
from app.infrastructures.repositories import Repository

class MenuItemRepository(Repository[MenuItem]):
    def __init__(self,session: AsyncSession) -> None:
        super().__init__(session=session,model=MenuItem)
    
    async def retrieve_by_name(self,item_name: str) -> Optional[MenuItem]:
        """
            Retrieve model instance by its name.
        """
        result = await self._session.execute(
            select(self._model).where(self._model.item_name == item_name)
        )
        return result.scalar_one_or_none()