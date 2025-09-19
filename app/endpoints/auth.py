from fastapi import APIRouter , Depends
from dependency_injector.wiring import inject , Provide

from app.container import Container
from app.services import AuthService
from app.core.schemas.user import UserLogin
from app.core.schemas.token import TokenResponse

router = APIRouter(prefix='/auth',tags=['Auth'])

@router.post('/login',response_model=TokenResponse)
@inject
async def validate_login(
    request: UserLogin,
    service: AuthService = Depends(Provide[Container.auth_service])
):
    """
        Route to validate user login.
    """
    return await service.validate_login(data=request.model_dump())