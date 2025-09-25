from enum import Enum

class PaymentType(Enum):
    cash = "cash"
    esewa = "esewa"

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"