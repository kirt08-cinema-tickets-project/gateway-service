from typing import Annotated
from google.protobuf.json_format import MessageToDict

from fastapi import APIRouter, Depends

from src.apps.shared.service import authorized
from src.apps.grpc_clients import refund_client

from src.apps.refund.schemas import CreateRefundRequest


router = APIRouter()

@router.post("/")
async def create_refund(
        data: CreateRefundRequest,
        payload: Annotated[dict[str, str], Depends(authorized)]
):
    user_id = payload.get("payload")
    grpc_response = await refund_client.CreateRefundRequest(
        booking_id = data.booking_id,
        user_id = user_id
    )
    return MessageToDict(grpc_response)
