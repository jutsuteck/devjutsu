import uuid
import redis.asyncio

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, RedisStrategy

from src.core.auth.user_manager import get_user_manager
from src.core.config.settings import get_settings
from src.models.v1.users import Member

settings = get_settings()

REDIS_URL = f"redis://{settings.redis_user}:{settings.redis_password}@{settings.redis_host}:{settings.redis_port}"

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

redis = redis.asyncio.from_url(REDIS_URL, decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)  # type: ignore


auth_backend = AuthenticationBackend(
    name="redis",
    transport=bearer_transport,
    get_strategy=get_redis_strategy
)

users = FastAPIUsers[Member, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = users.current_user(active=True)
