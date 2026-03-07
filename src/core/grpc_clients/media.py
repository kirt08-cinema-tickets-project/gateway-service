import grpc
from kirt08_contracts.media import media_pb2_grpc, media_pb2


class MediaClient:
    def __init__(self, host: str):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = media_pb2_grpc.MediaServiceStub(self._channel)

    async def upload(self, file_name: str, folder: str, content_type: str, data: bytes,
                     resize_width: int | None, resize_height: int | None):
        request = media_pb2.UploadRequest(
            file_name = file_name,
            folder = folder,
            content_type = content_type,
            data = data,
            resize_width = resize_width,
            resize_height = resize_height,
        )
        response = await self._stub.Upload(request)
        return response