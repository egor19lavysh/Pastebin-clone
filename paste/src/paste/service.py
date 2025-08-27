from .schemas import PasteSchema, PasteCreateSchema
from .repository import PasteRepository
from dataclasses import dataclass
from .models import Paste
from .enums import *


@dataclass
class PasteService:
    """
    Класс-сервис для модели данных Paste.
    :params repository - экземпляр класса PasteRepository
    """
    repository: PasteRepository

    async def get_pastes(self) -> list[PasteSchema]:
        pastes = await self.repository.get_pastes()
        orm_pastes = [await self._to_schema(paste) for paste in pastes]
        return orm_pastes
    
    async def get_paste(self, hash: str) -> PasteSchema | None:
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            orm_paste = await self._to_schema(paste)
            return orm_paste
        raise Exception("Paste is not found")

    async def create_paste(self, paste: PasteCreateSchema) -> str:
        paste_hash = await self.repository.create_paste(paste=paste)
        return paste_hash
    
    async def update_paste_title(self, hash: str, new_title: str) -> PasteSchema:
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            updated_paste = await self.repository.update_paste_title(hash=hash, new_title=new_title)
            orm_updated_paste = await self._to_schema(updated_paste)
            return orm_updated_paste
        raise Exception("Paste is not found")
    
    async def update_paste_text(self, hash: str, new_text: str) -> PasteSchema:
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            updated_paste = await self.repository.update_paste_text(hash=hash, new_text=new_text)
            orm_updated_paste = await self._to_schema(updated_paste)
            return orm_updated_paste
        raise Exception("Paste is not found")

    @staticmethod
    async def _validate_syntax(syntax: str) -> bool:
        """Проверяет, что значение есть в SyntaxType"""
        return syntax in [item.value for item in SyntaxType]
    
    async def update_paste_syntax(self, hash: str, new_syntax: str) -> PasteSchema:
        if not await self._validate_syntax(new_syntax):
            raise Exception("incorrect syntax")
        
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            updated_paste = await self.repository.update_paste_syntax(hash=hash, new_syntax=new_syntax)
            orm_updated_paste = await self._to_schema(updated_paste)
            return orm_updated_paste
        raise Exception("Paste is not found")

    @staticmethod
    async def _validate_expiration(time: str) -> bool:
        """Проверяет, что значение есть в ExpireAt"""
        return time in [item.value for item in ExpireAt]
    
    async def update_paste_expiration(self, hash: str, new_expiration: str) -> PasteSchema:
        if not await self._validate_expiration(new_expiration):
            raise Exception("incorrect value")
        
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            updated_paste = await self.repository.update_paste_expiration(hash=hash, new_expiration=new_expiration)
            orm_updated_paste = await self._to_schema(updated_paste)
            return orm_updated_paste
        raise Exception("Paste is not found")
    
    @staticmethod
    async def _validate_visibility(visibility: str) -> bool:
        """Проверяет, что значение есть в PasteVisibility"""
        return visibility in [item.value for item in PasteVisibility]

    async def update_paste_visibility(self, hash: str, new_visibility: str) -> PasteSchema:
        if not await self._validate_visibility(new_visibility):
            raise Exception("incorrect value")

        paste = await self.repository.get_paste(hash=hash)
        if paste:
            updated_paste = await self.repository.update_paste_visibility(hash=hash, new_visibility=new_visibility)
            orm_updated_paste = await self._to_schema(updated_paste)
            return orm_updated_paste
        raise Exception("Paste is not found")
    
    
    async def delete_paste(self, hash: str) -> None:
        paste = await self.repository.get_paste(hash=hash)
        if paste:
            await self.repository.delete_paste(hash=hash)
        else:
            raise Exception("Paste is not found")
    
    async def delete_all_pastes(self):
        await self.repository.delete_all_pastes()

    @staticmethod
    async def _to_schema(paste: Paste) -> PasteSchema:
        return PasteSchema.model_validate(paste, from_attributes=True)