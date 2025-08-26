from src.paste.repository import PasteRepository
from src.paste.service import PasteService
from typing import Annotated
from fastapi import Depends


async def get_paste_repository():
    return PasteRepository()

async def get_paste_service(paste_repository: Annotated[PasteRepository, Depends(get_paste_repository)]):
    return PasteService(repository=paste_repository)