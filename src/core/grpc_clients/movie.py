import grpc
from kirt08_contracts.movie import movie_pb2, movie_pb2_grpc


class MovieClient:
    def __init__(self, host: str, ):
        self._channel = grpc.aio.insecure_channel(host)
        self._stub = movie_pb2_grpc.MovieServiceStub(self._channel)

    async def ListMovies(self, category: str, random: bool, limit: int):
        request = movie_pb2.ListMoviesRequest(
            category = category,
            random = random,
            limit = limit
        )
        response = await self._stub.ListMovies(request)
        return response
    
    async def GetMovie(self, id: str | None = None, slug: str | None = None):
        if not id and not slug:
            raise ValueError
        
        request = movie_pb2.GetMovieRequest()
        if id:
            request.id = id
        else:
            request.slug = slug
        
        response = await self._stub.GetMovie(request)
        return response