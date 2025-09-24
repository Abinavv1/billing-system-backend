from sqlalchemy.ext.asyncio import AsyncSession

from .base import Repository
from app.infrastructures.models import Order

class OrderRepository(Repository[Order]):
    def __init__(self,session: AsyncSession) -> None:
        super().__init__(session=session,model=Order)