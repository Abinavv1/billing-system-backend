from dependency_injector import containers , providers

from app.core.settings import get_settings
from app.infrastructures.database.engine import Database
from app.infrastructures.database.meta import UserDBMeta
from app.infrastructures.repositories import UserRepository , MenuItemRepository
from app.services import UserService , AuthService , MenuItemService

settings = get_settings()

class Container(containers.DeclarativeContainer):
    """
        Dependency container
    """    
    wiring_config = containers.WiringConfiguration(packages=["app.endpoints"]) 
        
    database = providers.Singleton(
        Database,
        url=settings.DATABASE_URL,
        base=UserDBMeta
    )
    
    database_session = providers.Resource(
        lambda db_instance: db_instance.get_session(),
        db_instance=database
    )
    
    user_repo = providers.Factory(
        UserRepository,
        session=database_session
    )
    
    menu_item_repo = providers.Factory(
        MenuItemRepository,
        session=database_session
    )
    
    user_service = providers.Factory(
        UserService,
        user_repo=user_repo
    )
    
    auth_service = providers.Factory(
        AuthService,
        user_repo=user_repo
    )
    
    menu_item_service = providers.Factory(
        MenuItemService,
        menu_item_repo=menu_item_repo
    )
    


container = Container()
