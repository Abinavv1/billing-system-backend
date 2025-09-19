from pydantic import BaseModel

class Schema(BaseModel):
    """
        Base class from all schemas.
    """
    model_config = {
        "from_attributes": True,
        "extra":"ignore"
    }