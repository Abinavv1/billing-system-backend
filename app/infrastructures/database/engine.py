from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession , create_async_engine , async_sessionmaker

class Database:
    def __init__(
        self,
        url: str,
        base: DeclarativeBase
    ) -> None:
        self._url = url
        self._base = base
        
        self._engine = create_async_engine(url=self._url,echo=True)
        self._session_maker = async_sessionmaker(bind=self._engine,expire_on_commit=False)
    
    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession,None]:
        async with self._session_maker() as session:
            yield session
        
    async def create_tables(self) -> None:
        import app.infrastructures.models
        async with self._engine.begin() as conn:
            await conn.run_sync(self._base.metadata.create_all)
    
    async def drop_tables(self) -> None:
        import app.infrastructures.models
        async with self._engine.begin() as conn:
            await conn.run_sync(self._base.metadata.drop_all)
            
        