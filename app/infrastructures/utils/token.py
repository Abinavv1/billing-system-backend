from typing import Dict , Any
from datetime import datetime , timezone , timedelta
from authlib.jose import jwt , JoseError

from app.core.settings import get_settings

settings = get_settings()

_SECRET_KEY: str = settings.JWT_SECRET_KEY
_ALGORITHM: str = settings.JWT_ALGORITHM
_TOKEN_EXPIRY: int = settings.JWT_TOKEN_EXPIRY

async def generate_token(payload: Dict[str,Any]) -> str:
    """
        Generate a JWT token by encoding payload.
    """
    try:
        expire_time = datetime.now(timezone.utc) + timedelta(minutes=_TOKEN_EXPIRY)
        payload.update({
            "exp": expire_time,
            "iat": datetime.now(timezone.utc)
        })
        
        token = jwt.encode(
            header={"alg": _ALGORITHM},
            payload=payload,
            key=_SECRET_KEY
        )

        return token.decode("utf-8") if isinstance(token, bytes) else token
    except JoseError as e:
        raise JoseError(f"JWT generation failed: {str(e)}")

async def decode_token(token: str) -> Dict[str,Any]:
    """
        Decode token and extract payload.
    """
    try:
        claims = jwt.decode(token, _SECRET_KEY)
        claims.validate()
        return claims
    except JoseError as e:
        raise JoseError(f"JWT decoding failed: {str(e)}")