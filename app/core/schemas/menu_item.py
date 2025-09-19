from typing import Optional

from .base import Schema

class MenuItemCreate(Schema):
    item_name: str
    price: float
    
class MenuItemUpdate(Schema):
    item_name: Optional[str] = None
    price: Optional[float] = None

class MenuItemResponse(Schema):
    id: str
    item_name: str
    price: float