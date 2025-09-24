from typing import Optional

from .base import Schema

class MenuItemCreate(Schema):
    item_name: str
    price: float
    description: str
    is_available: bool
    
class MenuItemUpdate(Schema):
    item_name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    is_available: Optional[bool] = None

class MenuItemResponse(Schema):
    id: str
    item_name: str
    price: float
    description: str
    is_available: bool