from sqlalchemy.orm import mapped_column , Mapped
from sqlalchemy import String , Float

from .base import Model
from app.infrastructures.database.meta import UserDBMeta

class MenuItem(Model,UserDBMeta):
    """
        Class representing menu items.
    """
    __tablename__ = "menu_items"
    
    item_name: Mapped[str] = mapped_column(String(50),unique=True,index=True,nullable=False)
    price: Mapped[float] = mapped_column(Float,nullable=False)