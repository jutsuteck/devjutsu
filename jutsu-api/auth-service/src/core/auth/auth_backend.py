import uuid
import redis.asyncio

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, RedisStrategy

from src.core.auth.user_manager import get_user_manager
from src.models.v1.user import User

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

redis = redis.asyncio.from_url(
    "redis://user_token_database:6379", decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)  # type: ignore


auth_backend = AuthenticationBackend(
    name="redis",
    transport=bearer_transport,
    get_strategy=get_redis_strategy
)

users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
