import uuid
from typing import Dict , Any
from datetime import datetime

from sqlalchemy.orm import mapped_column , Mapped
from sqlalchemy import String , DateTime , func

class Model:
    """
        Base class for SQL model.
    """
    id: Mapped[str] = mapped_column(
        String(255),
        primary_key=True,
        index=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
    
    def update(self,data: Dict[str,Any]) -> "Model":
        for key, value in data.__dict__.keys():
            pass