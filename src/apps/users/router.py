from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.apps.grpc_clients import users_client

from src.apps.shared.service import authorized

from src.apps.users.shemas import GetMeResponse, PatchMeRequest


router = APIRouter()

@router.get("/me", 
            summary="Get inforamation about current logined user",
            description="Get inforamation about current logined user")
async def get_me(payload: Annotated[dict[str, str], Depends(authorized)]) -> GetMeResponse:
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


@router.patch("/me", 
              summary="Let you change user",
              description="Let you change your user's name, in future also avatar")
async def patch_me(
    data: PatchMeRequest,
    payload: Annotated[dict[str, str], Depends(authorized)]
) -> dict[str, bool]:
    user_id = payload.get("payload")

    result = True
    if data.name is not None:
        grpc_response = await users_client.patch_me(
            id = user_id,
            name = data.name
        )
        result = grpc_response.ok
    return {"message": result}


