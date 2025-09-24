from sqlalchemy.orm import mapped_column , Mapped
from sqlalchemy import Integer , ForeignKey , Float , String , Boolean

from .base import Model
from app.infrastructures.database.meta import UserDBMeta

class OrderItem(Model,UserDBMeta):
    __tablename__ = "order_items"
    
    menu_item: Mapped[str] = mapped_column(ForeignKey("menu_items.id"),nullable=False)
    quantity: Mapped[int] = mapped_column(Integer,nullable=False)

class Order(Model,UserDBMeta):
    __tablename__ = "orders"
    
    amount: Mapped[float] = mapped_column(Float,nullable=False)
    type: Mapped[str] = mapped_column(String,nullable=False)
    is_paid: Mapped[bool] = mapped_column(Boolean,default=False,nullable=False)