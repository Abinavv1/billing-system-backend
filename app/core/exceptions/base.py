class AppException(Exception):
    """
        Base class for custom exceptions.
    """
    def __init__(self,message: str,status: int) -> None:
        self.message = message
        self.status = status
        super().__init__(message)