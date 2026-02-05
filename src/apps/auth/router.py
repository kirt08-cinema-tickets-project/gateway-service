import grpc
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from kirt08_contracts.auth import auth_pb2
from kirt08_exceptions.exceptions import GrpcToHttp

from src.core.config import settings

from src.apps.auth.utils import Roles
from src.apps.grpc_clients import auth_client
from src.apps.shared.service import authorized, permission_guard
from src.apps.auth.schemas import SendOtpRequest, VerifyOtpRequest

router = APIRouter(prefix="/otp")


@router.post("/send", 
    summary="Send otp code", 
    description="Sends a verification code to the user phone number or email"
)
async def auth_send_otp(data : SendOtpRequest) -> dict[str, bool]:
    try:
        response = await auth_client.send_otp(data.identifier, data.type_identifier)
        return {
            "ok": response.ok,
        }
    except grpc.aio.AioRpcError as e:
            http_status = GrpcToHttp[e.code().name].value
            raise HTTPException(status_code=http_status, detail=e.details())
    

@router.post("/verify",
    summary="Verify otp code",
    description="Verifies the code sent to the user phone number or email and returns a access token",
)
async def auth_verify_otp(data : VerifyOtpRequest, response : Response) -> dict[str, str]:
    try:
        grpc_response : auth_pb2.VerifyOtpResponse  = await auth_client.verify_otp(data.identifier, data.type_identifier, data.code)
        response.set_cookie(
            key = "refreshToken",
            value = grpc_response.refresh_token,
            httponly = True,
            secure = True if settings.mode.mode == "production" else False,
            domain = settings.cookies.domain if settings.mode.mode == "production" else None,
            samesite = 'lax',
            max_age = 24 * 60 * 60, # 1 day
            expires = 24 * 60 * 60, # 1 day
        )
        return {"access_token": grpc_response.access_token}
    except grpc.aio.AioRpcError as e:
        http_status = GrpcToHttp[e.code().name].value
        raise HTTPException(status_code=http_status, detail=e.details())


@router.post("/refresh",
    summary="Refresh access token",
    description="Renews access token using refresh token from cookies",
)
async def refresh(response : Response, refreshToken : Annotated[str | None, Cookie()] = None) -> dict[str, str]:
    try:
        grpc_response : auth_pb2.RefreshResponse = await auth_client.refresh(refreshToken)
        response.set_cookie(
            key = "refreshToken",
            value = grpc_response.refresh_token,
            httponly = True,
            secure = True if settings.mode.mode == "production" else False,
            domain = settings.cookies.domain if settings.mode.mode == "production" else None,
            samesite = 'lax',
            max_age=24 * 60 * 60 * 1000, # 1 day
            expires = 24 * 60 * 60, # 1 day
        )
        return {"access_token": grpc_response.access_token}
    except grpc.aio.AioRpcError as e:
         http_status = GrpcToHttp[e.code().name].value
         raise HTTPException(status_code=http_status, detail=e.details())


@router.post("/logout",
    summary="Logout",
    description="Clears the refresh token cookie and logs the user out"
)
async def logout(response : Response) -> dict[str, bool]:
    response.delete_cookie(
        key = "refreshToken",
        domain = settings.cookies.domain if settings.mode.mode == "production" else None,
    )
    return {"ok": True}

@router.post("/test")
async def test_func(user_id : Annotated[str, Depends(authorized)]):
    return user_id

@router.post("/test-getaccount", dependencies=[Depends(permission_guard(Roles.ADMIN))])
async def test_get_account():
    # grpc_response = await account_client.get_account(user_id)
    return {"response": "ok"}