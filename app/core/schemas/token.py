from .base import Schema

class TokenResponse(Schema):
    token: str
    token_type: str = "Bearer"