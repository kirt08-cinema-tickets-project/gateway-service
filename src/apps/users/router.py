import grpc
from typing import Annotated
from kirt08_exceptions.exceptions import GrpcToHttp

from fastapi import APIRouter, Depends, HTTPException

from src.apps.grpc_clients import users_client

from src.apps.shared.service import authorized

from src.apps.users.shemas import GetMeResponse


router = APIRouter()

@router.get("/me")
async def get_me(payload: Annotated[dict[str, str], Depends(authorized)]) -> GetMeResponse:
    try:
        user_id = payload.get("payload")
        grpc_response = await users_client.get_me(user_id)
        user = GetMeResponse(
            id = grpc_response.user.id,
            name = grpc_response.user.name if grpc_response.user.name != "" else None, 
            avatar = grpc_response.user.avatar if grpc_response.user.avatar != "" else None,
            phone = grpc_response.user.phone if grpc_response.user.phone != "" else None,
            email = grpc_response.user.email if grpc_response.user.email != "" else None 
        )
        return user
    except grpc.aio.AioRpcError as e:
        http_status = GrpcToHttp[e.code().name].value
        raise HTTPException(status_code=http_status, detail=e.details())
