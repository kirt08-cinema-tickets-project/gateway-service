from typing import Annotated

from fastapi import APIRouter, Depends

from src.apps.grpc_clients import account_client
from src.apps.shared.service import authorized

from src.apps.account.schemas import (
    InitEmailChangeRequest,
    ConfirmEmailChangeRequest,
    InitPhoneChangeRequest,
    ConfirmPhoneChangeRequest,
) 


router = APIRouter()
 
@router.post("/email/init")
async def init_email_change(data : InitEmailChangeRequest, payload : Annotated[dict[str, str], Depends(authorized)]):
    user_id = int(payload.get("payload"))
    grpc_response = await account_client.init_email_change(data.email, user_id)
    return grpc_response.ok
    
@router.post("/email/confirm")
async def confirm_email_change(data : ConfirmEmailChangeRequest, payload : Annotated[dict[str, str], Depends(authorized)]):
    user_id = int(payload.get("payload"))
    grpc_response = await account_client.confirm_email_change(data.email, data.code, user_id)
    return grpc_response

    
@router.post("/phone/init")
async def init_phone_change(data : InitPhoneChangeRequest, payload : Annotated[dict[str, str], Depends(authorized)]):
    user_id = int(payload.get("payload"))
    grpc_response = await account_client.init_phone_change(data.phone, user_id)
    return grpc_response.ok
    

@router.post("/phone/confirm")
async def confirm_phone_change(data : ConfirmPhoneChangeRequest, payload : Annotated[dict[str, str], Depends(authorized)]):
    user_id = int(payload.get("payload"))
    grpc_response = await account_client.confirm_phone_change(data.phone, data.code, user_id)
    return grpc_response
    
