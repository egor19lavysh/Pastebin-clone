from redis import asyncio as asyncredis
from src.config import settings


async def get_redis_connection() -> asyncredis.Redis:
    redis = asyncredis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return redis

