import grpc

from kirt08_contracts.refund import refund_pb2_grpc, refund_pb2


class RefundClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = refund_pb2_grpc.RefundServiceStub(self._channel)
        
    async def CreateRefundRequest(
            self,
            booking_id: str,
            user_id: str
    ):
        request = refund_pb2.CreateRefundRequest(
            booking_id = booking_id,
            user_id = user_id
        )
        response = await self._stub.CreateRefund(request)

        return response
    
    async def ProcessRefundEvent(
            self, 
            event: str,
            provider_refund_id,
            status: str
    ):
        request = refund_pb2.ProcessRefundEventRequest(
            event = event,
            provider_refund_id = provider_refund_id,
            status = status
        )

        response = await self._stub.ProcessRefundEvent(request)

        return response