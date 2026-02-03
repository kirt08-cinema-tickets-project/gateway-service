from typing import Annotated

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials

from src.core.utils import token, bearer_shema

async def authorized(credentials : Annotated[HTTPAuthorizationCredentials, Depends(bearer_shema)]) -> dict[str, str]:
    user_token : str = credentials.credentials
    print(user_token)
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
    