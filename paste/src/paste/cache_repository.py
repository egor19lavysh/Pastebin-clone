from dataclasses import dataclass
from redis import asyncio as aioredis
from .schemas import PasteSchema
import json


@dataclass
class PasteCache:
    """
    Класс-репозиторий для хранения кэша в Redis.
    """
    redis: aioredis.Redis

    async def set_pastes(self, pastes: list[PasteSchema]) -> None:
        pastes_json = [paste.model_dump_json() for paste in pastes]
        async with self.redis as redis:
            await redis.lpush("pastes", *pastes_json)

    async def get_pastes(self) -> list[PasteSchema]:
        async with self.redis as redis:
            pastes_json = await redis.lrange("pastes", 0, -1)
            return [PasteSchema.model_validate_json(paste) for paste in pastes_json]
        
    async def get_paste(self, hash: str) -> PasteSchema | None:
        async with self.redis as redis:
            paste_json = await redis.get(f"paste:{hash}") # Возможно нужно будет заменить на hash:hash
            if paste_json:
                return PasteSchema.model_validate_json(paste_json)
            return None

    async def set_paste(self, paste: PasteSchema, expire_seconds: int = 600) -> None:
        async with self.redis as redis:
            await redis.setex(
                f"paste:{paste.hash}",
                expire_seconds,
                paste.model_dump_json()
            )

    async def delete_paste(self, hash: str) -> None:
        async with self.redis as redis:
            await redis.delete(f"paste:{hash}")