from src.core.config import settings
from src.core.grpc_clients import (
    AuthClient,
    AccountClient,
    UsersClient,
)


auth_url = settings.auth.host + ":" + settings.auth.port
auth_client = AuthClient(auth_url)
account_client = AccountClient(auth_url)

users_url = settings.users.host + ":" + settings.users.port
users_client = UsersClient(users_url)
