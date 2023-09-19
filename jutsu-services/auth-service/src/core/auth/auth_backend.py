import uuid
import redis.asyncio

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    RedisStrategy
)

from src.core.auth.user_manager import get_user_manager
from src.core.config.settings import get_settings
from src.models.v1.users import Member

settings = get_settings()

redis_user = settings.redis.redis_user
redis_password = settings.redis.redis_password
redis_host = settings.redis.redis_host
redis_port = settings.redis.redis_port

REDIS_URL = f"redis://{redis_user}:{redis_password}@{redis_host}:{redis_port}"

bearer_transport = BearerTransport(tokenUrl="auth/login")

redis = redis.asyncio.from_url(REDIS_URL, decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    lifetime_seconds = 30 * 24 * 60 * 60  # This is one month in seconds
    return RedisStrategy(redis, lifetime_seconds=lifetime_seconds)


auth_backend = AuthenticationBackend(
    name="redis",
    transport=bearer_transport,
    get_strategy=get_redis_strategy
)

users = FastAPIUsers[Member, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = users.current_user(active=True, verified=True)
