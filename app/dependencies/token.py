from typing import Dict, Any

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from authlib.jose import JoseError

from app.core.exceptions import ForbiddenException
from app.infrastructures.utils.token import decode_token

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Dict[str, Any]:
    """
        Get current logged in user from JWT token.
    """
    token = credentials.credentials
    try:
        return await decode_token(token)
    except (Exception,JoseError) as e:
        raise ForbiddenException(message="Forbidden")