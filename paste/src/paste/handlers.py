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


@router.get("/{hash}")
async def get_paste(service: Annotated[PasteService, Depends(get_paste_service)],
                    hash: str) -> PasteSchema | None:
    paste = await service.get_paste(hash=hash)
    return paste


@router.delete("/")
async def delete_pastes(service: Annotated[PasteService, Depends(get_paste_service)]) -> None:
    await service.delete_all_pastes()


@router.delete("/{hash}")
async def delete_paste(service: Annotated[PasteService, Depends(get_paste_service)],
                        hash: str) -> None:
    await service.delete_paste(hash=hash)


@router.patch("/{hash}/title")
async def update_paste_title(service: Annotated[PasteService, Depends(get_paste_service)],
                       hash: str, new_title: str) -> PasteSchema:
    return await service.update_paste_title(hash=hash, new_title=new_title)

@router.patch("/{hash}/text")
async def update_paste_text(service: Annotated[PasteService, Depends(get_paste_service)],
                       hash: str, new_text: str) -> PasteSchema:
    return await service.update_paste_text(hash=hash, new_text=new_text)

@router.patch("/{hash}/syntax")
async def update_paste_syntax(service: Annotated[PasteService, Depends(get_paste_service)],
                       hash: str, new_syntax: str) -> PasteSchema:
    return await service.update_paste_syntax(hash=hash, new_syntax=new_syntax)

@router.patch("/{hash}/expiration")
async def update_paste_expiration(service: Annotated[PasteService, Depends(get_paste_service)],
                       hash: str, new_expiration: str) -> PasteSchema:
    return await service.update_paste_expiration(hash=hash, new_expiration=new_expiration)

@router.patch("/{hash}/visibility")
async def update_paste_visibility(service: Annotated[PasteService, Depends(get_paste_service)],
                       hash: str, new_visibility: str) -> PasteSchema:
    return await service.update_paste_visibility(hash=hash, new_visibility=new_visibility)
    
