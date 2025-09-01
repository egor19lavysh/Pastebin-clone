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
    PASTE_PREFIX: str = "paste_"

    async def set_pastes(self, pastes: list[PasteSchema], expiration: int = 600) -> None:
        for paste in pastes:
            await self.set_paste(paste=paste, expiration=expiration)
        
    async def get_pastes(self) -> list[PasteSchema]:
        pattern = self.PASTE_PREFIX + "*"
        
        async with self.redis as redis:
            cursor = 0
            pastes = []
            
            while True:
                cursor, keys = await redis.scan(cursor=cursor, match=pattern, count=100)
                
                for paste_key in keys:
                    paste_json = await redis.get(paste_key)
                    if paste_json is not None:
                        try:
                            orm_paste = PasteSchema.model_validate_json(paste_json)
                            pastes.append(orm_paste)
                        except Exception:
                            continue
                
                if cursor == 0:
                    break
                    
            return pastes

        
    async def get_paste(self, hash: str) -> PasteSchema | None:
        async with self.redis as redis:
            paste_json = await redis.get(self.PASTE_PREFIX + hash)
            if paste_json is not None:
                try:
                    return PasteSchema.model_validate_json(paste_json)
                except Exception:
                    return None
            return None

    async def set_paste(self, paste: PasteSchema, expiration: int = 600) -> None:
        paste_json = paste.model_dump_json()
        paste_hash = paste.hash
        async with self.redis as redis:
            await redis.setex(name=self.PASTE_PREFIX + paste_hash, time=expiration, value=paste_json)

    async def delete_paste(self, hash: str) -> None:
        async with self.redis as redis:
            if await redis.exists(self.PASTE_PREFIX + hash):
                await redis.delete(self.PASTE_PREFIX + hash)

    async def update_paste_title(self):
        pass

    
    async def update_paste_text(self):
        pass


    async def update_paste_syntax(self):
        pass


    async def update_paste_expiration(self):
        pass


    async def update_paste_visibility(self):
        pass

