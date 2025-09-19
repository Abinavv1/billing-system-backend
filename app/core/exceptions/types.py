from .base import AppException

class ConflictException(AppException):
    """
        Exception for conflict in resources.
    """
    def __init__(self,message: str = "Conflict cooured",status: int = 409) -> None:
        super().__init__(message=message,status=status)

class NotFoundException(AppException):
    """
        Exception for resources not found.
    """
    def __init__(self,message: str = "Not Found",status: int = 404) -> None:
        super().__init__(message=message,status=status)

class InternalServerException(AppException):
    """
        Exception for generic server exception.
    """
    def __init__(self,message: str = "Internal Server Error",status: int = 500) -> None:
        super().__init__(message=message,status=status)

class LoginException(AppException):
    """
        Exception for login exceptions.
    """
    def __init__(self,message: str = "Login failed",status: int = 401) -> None:
        super().__init__(message=message,status=status)
        
class ForbiddenException(AppException):
    """
        Exception for login exceptions.
    """
    def __init__(self,message: str = "Forbidden",status: int = 403) -> None:
        super().__init__(message=message,status=status)