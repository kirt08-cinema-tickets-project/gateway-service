import grpc

from fastapi import APIRouter, HTTPException
from kirt08_contracts import auth_pb2
from kirt08_exceptions.exceptions import GrpcToHttp

from src.core.grpc_clients import AuthClient
from src.core.config import settings

from src.apps.auth.schemas import SendOtpRequest, VerifyOtpRequest

router = APIRouter(prefix="/otp")

auth_url = str(settings.auth.host) + ":" + str(settings.auth.port)
auth_client = AuthClient(auth_url)


@router.post("/send", 
    summary="Send otp code", 
    description="Sends a verification code to the user phone number or email"
)
async def auth_send_otp(data : SendOtpRequest):
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
async def auth_verify_otp(data : VerifyOtpRequest):
    try:
        grpc_response : auth_pb2.VerifyOtpResponse  = await auth_client.verify_otp(data.identifier, data.type_identifier, data.code)
        return {
            "access_token": grpc_response.access_token,
            "refresh_token": grpc_response.refresh_token,
        }
    except grpc.aio.AioRpcError as e:
        http_status = GrpcToHttp[e.code().name].value
        raise HTTPException(status_code=http_status, detail=e.details())

