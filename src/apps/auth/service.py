from typing import Annotated

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials

from kirt08_contracts.account.account_pb2 import Role as ProtoRole

from src.core.utils import token, bearer_shema

from src.apps.auth.utils import Roles
from src.apps.auth.grpc_clients import account_client

async def authorized(credentials : Annotated[HTTPAuthorizationCredentials, Depends(bearer_shema)]) -> dict[str, str]:
    user_token : str = credentials.credentials
    if len(user_token) == 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is empty",
        )
    res = token.verify_token(user_token)
    if res.get("valid") is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=res.get("reason"),
        )
    return {"payload": res.get("payload")}

def permission_guard(*allowed_roles: Roles):
    async def guard(payload: dict = Depends(authorized)):
        user_id = payload["payload"]

        if not allowed_roles:
            return True

        user = await account_client.get_account(int(user_id))
        user_role = Roles[ProtoRole.Name(user.role)]

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )

        return True

    return guard
    
    