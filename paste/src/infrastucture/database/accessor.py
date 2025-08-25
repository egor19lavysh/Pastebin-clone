from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings


async def get_mongo_client():
    client = AsyncIOMotorClient(settings.MONGO_URL)
    return client