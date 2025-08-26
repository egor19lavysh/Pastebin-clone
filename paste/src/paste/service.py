from .schemas import PasteSchema, PasteCreateSchema
from .repository import PasteRepository
from dataclasses import dataclass
from .models import Paste


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
    
    async def create_paste(self, paste: PasteCreateSchema) -> str:
        paste_hash = await self.repository.create_paste(paste=paste)
        return paste_hash
    
    async def delete_all_pastes(self):
        await self.repository.delete_all_pastes()

    @staticmethod
    async def _to_schema(paste: Paste) -> PasteSchema:
        return PasteSchema.model_validate(paste, from_attributes=True)