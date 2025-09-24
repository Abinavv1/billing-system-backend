from dependency_injector import containers , providers

from app.core.settings import get_settings
from app.infrastructures.database.engine import Database
from app.infrastructures.database.meta import UserDBMeta
from app.infrastructures.gateways.payment import EsewaGateway
from app.infrastructures.repositories import UserRepository , MenuItemRepository , OrderRepository
from app.services import UserService , AuthService , MenuItemService , OrderService

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
    
    order_repo = providers.Factory(
        OrderRepository,
        session=database_session
    )
    
    esewa_gateway = providers.Singleton(
        EsewaGateway
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
    
    order_service = providers.Factory(
        OrderService,
        menu_item_repo=menu_item_repo,
        order_repo=order_repo,
        payment_gateway=esewa_gateway
    )
    


container = Container()
