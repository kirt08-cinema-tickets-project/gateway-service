from fastapi import APIRouter

from kirt08_contracts.hall import hall_pb2
from google.protobuf.json_format import MessageToDict

from src.apps.grpc_clients import hall_client

from src.apps.halls.shemas import CreateHallRequest


router = APIRouter()

@router.post("/")
async def create_hall(data: CreateHallRequest):
    grpc_response = await hall_client.CreateHall(
        name = data.name,
        theater_id = data.theater_id,
        layouts = [
            hall_pb2.RowLayout(
                row=row.row,
                columns=row.columns,
                type=row.type,
                price=row.price
            )
            for row in data.layouts
        ]
    )
    return MessageToDict(grpc_response)

@router.get("/")
async def get_by_id(id: str):
    grpc_reponse = await hall_client.GetHall(
        id = id
    )
    return MessageToDict(grpc_reponse)