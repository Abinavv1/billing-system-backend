from sqlalchemy.orm import mapped_column , Mapped
from sqlalchemy import String , Boolean

from .base import Model
from app.infrastructures.database.meta import UserDBMeta

class User(Model,UserDBMeta):
    """
        Class representing user in database.
    """
    __tablename__ = "users"
    
    first_name: Mapped[str] = mapped_column(String(50),nullable=False)
    last_name: Mapped[str] = mapped_column(String(50),nullable=False)
    email: Mapped[str] = mapped_column(String(255),unique=True,index=True,nullable=False)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean,default=False,nullable=False)