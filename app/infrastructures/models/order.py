from sqlalchemy.orm import mapped_column , Mapped
from sqlalchemy import Float , Enum

from .base import Model
from app.core.enums.payment import PaymentStatus
from app.infrastructures.database.meta import UserDBMeta

class Order(Model,UserDBMeta):
    __tablename__ = "orders"
    
    amount: Mapped[float] = mapped_column(Float,nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus),
        name="payment_status",
        default=PaymentStatus.PENDING,
        nullable=False)