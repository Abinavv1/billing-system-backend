from typing import Optional
from .base import Schema

class OrderProcessData(Schema):
    """
        Schema for process order data.
    """
    id: str
    quantity: int

class OrderResponse(Schema):
    """
        Schema for order response data.
    """
    id: str
    amount: float
    type: str
    is_paid: bool

class OrderUpdate(Schema):
    """
        Schema for order update data.
    """
    amount: Optional[float] = None
    type: Optional[str] = None
    is_paid: Optional[bool] = None