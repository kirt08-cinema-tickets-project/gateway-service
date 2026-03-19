import grpc
from kirt08_contracts.payment import payment_pb2, payment_pb2_grpc

from src.apps.shared.schemas import SeatType


def mapper_seat_type(data: list[SeatType]) -> list[payment_pb2.SeatInput]:
    return [
        payment_pb2.SeatInput(
            seat_id = seat.seat_id,
            price = seat.price
        )
        for seat in data
    ]


class PaymentClient:
    def __init__(self, host: str):
        self._connection = grpc.aio.insecure_channel(host)
        self._stub = payment_pb2_grpc.PaymentServiceStub(self._connection)

    async def CreatePayment(
        self,
        user_id: str,
        screening_id: str,
        seats: list,
        save_payment_method: bool,
        payment_method_id: str | None = None
    ):
        request = payment_pb2.CreatePaymentRequest(
            user_id = user_id,
            screening_id = screening_id,
            seats = mapper_seat_type(seats),
            payment_method_id = payment_method_id,
            save_payment_method = save_payment_method
        )
        response: payment_pb2.CreatePaymantResponse = await self._stub.CreatePayment(request)
        return response

    async def ProcessPaymentEvent(
        self,
        event: str,
        payment_id: str,
        booking_id: str,
        user_id: str,
        save_payment_method: bool,
        provider_method_id: str,
        card_first6: str,
        card_last4: str,
        bank: str,
        brand: str
    ) -> payment_pb2.ProcessPaymentEventResponse:
        request = payment_pb2.ProcessPaymentEventRequest(
            event = event,
            payment_id = payment_id,
            booking_id = booking_id,
            user_id = user_id,
            save_payment_method = save_payment_method,
            provider_method_id = provider_method_id,
            card_first6 = card_first6,
            card_last4 = card_last4,
            bank = bank,
            brand = brand
        )
        response: grpc.ProcessPaymentEventResponse = await self._stub.ProcessPaymentEvent(request)
        return response
    
    async def GetUserPaymentMethods(
            self,
            user_id: str
    ) -> payment_pb2.GetUserPaymentMethodsResponse:
        request = payment_pb2.GetUserPaymentMethodsRequest(
            user_id = user_id
        )
        response: payment_pb2.GetUserPaymentMethodsResponse = await self._stub.GetUserPaymentMethods(request)
        return response

    async def DeleteUserPaymentMethod(
            self,
            user_id: str,
            method_id: str
    ):
        request = payment_pb2.DeleteUserPaymentMethodRequest(
            user_id = user_id,
            method_id = method_id
        )
        response: payment_pb2.DeleteUserPaymentMethodResponse = await self._stub.DeleteUserPaymentMethod(request)
        return response