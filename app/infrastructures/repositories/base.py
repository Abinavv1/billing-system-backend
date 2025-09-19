from typing import Generic , TypeVar , Type , Dict , Any , Optional , List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructures.models import Model

T = TypeVar("T",bound=Model)

class Repository(Generic[T]):
    def __init__(self,session: AsyncSession,model: Type[T]) -> None:
        self._session = session
        self._model = model
    
    async def commit(self) -> None:
        """
            Commit changes to database.
        """
        await self._session.commit()
    
    async def rollback(self) -> None:
        """
            rollback flushed changes from database.
        """
        await self._session.rollback()
        
    async def create(self,data: Dict[str,Any]) -> T:
        """
            Create a model instance
        """
        instance = self._model(**data)
        self._session.add(instance)
        await self._session.flush()
        await self._session.refresh(instance)
        return instance
    
    async def retrieve_by_id(self,id: str) -> Optional[T]:
        """
            Retrieve a model instance by its ID.
        """
        result = await self._session.get(self._model,id)
        return result
    
    async def retrieve_all(self) -> List[T]:
        """
            Retrieve a list of all model instances.        
        """
        result = await self._session.execute(select(self._model))
        return result.scalars().all()

    async def update(self,updated: T) -> T:
        """
            Update a existing model instance with new data.
        """
        self._session.add(updated)
        await self._session.flush()
        await self._session.refresh(updated)
        return updated
    
    async def delete(self,instance: T) -> None:
        """
            Delete a exisitng model instance.
        """
        await self._session.delete(instance)
        await self._session.flush()
