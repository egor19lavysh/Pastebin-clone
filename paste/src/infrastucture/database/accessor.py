from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings
from src.paste.models import Paste


async def init_mongo() -> None:
    client = AsyncIOMotorClient(settings.MONGO_URL)
    await init_beanie(database=client[settings.MONGO_DB_NAME], document_models=[Paste])