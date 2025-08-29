from src.paste.repository import PasteRepository
from src.paste.service import PasteService
from typing import Annotated
from fastapi import Depends
from redis.asyncio import Redis
from src.infrastucture.cache import get_redis_connection
from src.paste.cache_repository import PasteCache


async def get_paste_repository():
    return PasteRepository()

async def get_paste_service(paste_repository: Annotated[PasteRepository, Depends(get_paste_repository)]):
    return PasteService(repository=paste_repository)

async def get_cache_repository(redis: Annotated[Redis, Depends(get_redis_connection)]) -> PasteCache:
    return PasteCache(redis=redis)