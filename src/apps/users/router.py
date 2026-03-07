import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status

from src.apps.grpc_clients import users_client, media_client

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


@router.patch("@me/name", 
              summary="Let you change user",
              description="Let you change your user's name, in future also avatar")
async def patch_me_name(
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


@router.patch("@me/avatar", 
              summary="Update user avatar",
              description="Uploads a new avatar for the authenticated user")
async def patch_me_avatar(
    file: Annotated[UploadFile, File()],
    payload: Annotated[dict[str, str], Depends(authorized)]
):
    if file.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Not supported extension"
        )
    
    file_bytes = await file.read()

    if len(file_bytes) > 10 * 1024 * 1024: # = 10 Mb
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "File is too large"
        )
    
    media_grpc_response = await media_client.upload(
        file_name = secrets.token_hex(16),
        folder = "users",
        content_type = file.content_type,
        data = file_bytes,
        resize_width = 512,
        resize_height = 512
    )
    users_grpc_response = await users_client.patch_me(id = payload.get("payload"), avatar = media_grpc_response.key)
    return {
        "ok": users_grpc_response.ok
    }
    