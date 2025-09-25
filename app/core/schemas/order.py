from typing import Optional
from .base import Schema

class OrderProcessData(Schema):
    """
        Schema for process order data.
    """
    item_id: str
    quantity: int

class OrderResponse(Schema):
    """
        Schema for order response data.
    """
    id: str
    amount: float
    status: str

class OrderUpdate(Schema):
    """
        Schema for order update data.
    """
    amount: Optional[float] = None
    status: str