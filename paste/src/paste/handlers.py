from fastapi import APIRouter, Depends
from .schemas import PasteCreateSchema, PasteSchema
from .service import PasteService
from typing import Annotated
from src.dependencies import get_paste_service

router = APIRouter(prefix="/paste", tags=["pastes"])

@router.post("/")
async def create_paste(paste: PasteCreateSchema,
                       service: Annotated[PasteService, Depends(get_paste_service)]) -> str:
    paste_hash = await service.create_paste(paste=paste)
    return paste_hash


@router.get("/")
async def get_pastes(service: Annotated[PasteService, Depends(get_paste_service)]) -> list[PasteSchema]:
    pastes = await service.get_pastes()
    return pastes

@router.delete("/")
async def delete_pastes(service: Annotated[PasteService, Depends(get_paste_service)]) -> list[PasteSchema]:
    await service.delete_all_pastes()



@router.put("/{hash}")
async def update_paste(hash: str):
    pass


@router.delete("/{hash}")
async def delete_paste(hash: str):
    pass