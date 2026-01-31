from fastapi import APIRouter

from src.core.grpc_clients import AuthClient
from src.core.config import settings

from src.apps.auth.schemas import SendOtpRequest

router = APIRouter(prefix="/auth")

auth_url = str(settings.auth.host) + ":" + str(settings.auth.port)
auth_client = AuthClient(auth_url)


@router.post("/send", 
    summary="Send otp code", 
    description="Sends a verification code to the user phone number or email"
)
async def auth_send_otp(data : SendOtpRequest):
    response = await auth_client.send_otp(data.identifier, data.type_identifier)
    return {
        "ok": response.ok,
    }
    
    
