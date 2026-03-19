from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import payment_client

from src.apps.shared.service import authorized

from src.apps.payment.shemas import InitPaymentRequest


router = APIRouter()

@router.post("/init")
async def init_payment(
    data: InitPaymentRequest,
    payload: Annotated[dict[str, str], Depends(authorized)]
):
    grpc_response = await payment_client.CreatePayment(
        user_id = payload.get("payload"),
        screening_id = data.screening_id,
        seats = data.seats,
        save_payment_method = data.save_payment_method,
        payment_method_id = data.payment_method_id
    )

    return MessageToDict(grpc_response)


@router.post("/yookassa")
async def yookassa_handler(request: Request):
    data = await request.json()
    print(data)

    event: str = data.get("event")
    if not event:
        return {"ok": False}
    
    if event.startswith("payment."):
        obj = data.get("object", {})
        metadata = obj.get("metadata", {})
        payment_method = obj.get("payment_method", {})
        card = payment_method.get("card", {})
        card_product = card.get("card_product", {})

        grpc_response = await payment_client.ProcessPaymentEvent(
            event=event,
            payment_id=metadata.get("payment_id"),
            booking_id=metadata.get("booking_id"),
            user_id=metadata.get("user_id"),

            save_payment_method=payment_method.get("saved"),
            provider_method_id=payment_method.get("id"),

            card_first6=card.get("first6"),
            card_last4=card.get("last4"),

            bank = card_product.get("name") if card_product.get("name") else "Unknown",
            brand = card.get("card_type")
        )

    elif event.startswith("refaund."):
        ...

    return grpc_response.ok


@router.get("/method/all")
async def get_user_payment_methods(payload: Annotated[dict[str, str], Depends(authorized)]):
    user_id = payload.get("payload")
    grpc_response = await payment_client.GetUserPaymentMethods(user_id = user_id)
    return MessageToDict(grpc_response)


@router.delete("/method")
async def delete_user_payment_method(   
    method_id: Annotated[str, Query(...)],
    payload: Annotated[dict[str, str], Depends(authorized)]
):
    user_id = payload.get("payload")
    grpc_response = await payment_client.DeleteUserPaymentMethod(
        user_id = user_id,
        method_id = method_id
    )
    return MessageToDict(grpc_response)