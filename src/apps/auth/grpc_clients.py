from src.core.config import settings
from src.core.grpc_clients import AuthClient
from src.core.grpc_clients import AccountClient


auth_url = str(settings.auth.host) + ":" + str(settings.auth.port)
auth_client = AuthClient(auth_url)
account_client = AccountClient(auth_url)
