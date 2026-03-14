from src.core.config import settings
from src.core.grpc_clients import (
    AuthClient,
    AccountClient,
    UsersClient,
    MediaClient,
    MovieClient,
    CategoryClient,
    TheaterClient,
    HallClient,
    SeatsClient,
)


auth_url = settings.auth.host + ":" + settings.auth.port
auth_client = AuthClient(auth_url)
account_client = AccountClient(auth_url)

users_url = settings.users.host + ":" + settings.users.port
users_client = UsersClient(users_url)

media_url = settings.media.host + ":" + settings.media.port
media_client = MediaClient(media_url)

movie_url = settings.movie.host + ":" + settings.movie.port
movie_client = MovieClient(movie_url)

category_client = CategoryClient(movie_url)

theater_url = settings.theater.host + ":" + settings.theater.port
theater_client = TheaterClient(theater_url)

hall_client = HallClient(theater_url)

seats_client = SeatsClient(theater_url)