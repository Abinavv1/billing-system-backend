from .base import Schema

class OrderProcessData(Schema):
    """
        Schema for process order data.
    """
    id: str
    quantity: int