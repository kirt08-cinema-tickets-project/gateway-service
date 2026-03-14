from typing import Annotated
from fastapi import APIRouter, Path

from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import seats_client

from src.apps.seats.shemas import (
    GetSeatResponse,
    ListSeatsResponse
)


router = APIRouter()

@router.get("/{id}")
async def get_seat_by_id(id: Annotated[str, Path()]) -> GetSeatResponse:
    grpc_response = await seats_client.GetSeat(id = id)
    return MessageToDict(grpc_response)


@router.get("/{hall_id}/{screening_id}")
async def get_list_of_seats(
    hall_id: Annotated[str, Path(example="d49a85d2-3ca4-4391-a48f-e7ccbb54e09b")],
    screening_id: Annotated[str, Path(example="123456")]
) -> ListSeatsResponse:
    grpc_response = await seats_client.ListSeatsRequest(
        hall_id = hall_id,
        screening_id = screening_id
    )
    return MessageToDict(grpc_response)