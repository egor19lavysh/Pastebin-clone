import hashlib
import secrets
from datetime import datetime
from .models import Paste
from .schemas import PasteCreateSchema

class PasteRepository:
    """
    Класс-репозиторий для модели данных Paste.
    """

    async def get_pastes(self) -> list[Paste]:
        pastes = await Paste.find_all().to_list()
        return list(pastes)

    async def get_paste(self, hash: str) -> Paste | None:
        paste = await Paste.find_one(Paste.hash == hash)
        return paste

    async def create_paste(self, paste: PasteCreateSchema) -> str:
        new_hash = self._generate_hash(title=paste.title)
        new_paste = Paste(
            hash=new_hash,
            title=paste.title,
            text=paste.text,
            syntax=paste.syntax,
            expires_at=paste.expires_at,
            visibility=paste.visibility
        )

        await new_paste.insert()

        return new_hash

    async def update_paste_title(self, hash: str, new_title: str) -> Paste:
        paste = await self.get_paste(hash=hash)
        await paste.set({Paste.title: new_title})

        return paste
    
    async def update_paste_text(self, hash: str, new_text: str) -> Paste:
        paste = await self.get_paste(hash=hash)
        await paste.set({Paste.text: new_text})

        return paste
    
    async def update_paste_syntax(self, hash: str, new_syntax: str) -> Paste:
        paste = await self.get_paste(hash=hash)
        await paste.set({Paste.syntax: new_syntax})

        return paste
    
    async def update_paste_expiration(self, hash: str, new_expiration: str) -> Paste:
        paste = await self.get_paste(hash=hash)
        await paste.set({Paste.expires_at: new_expiration})

        return paste
    
    async def update_paste_visibility(self, hash: str, new_visibility: str) -> Paste:
        paste = await self.get_paste(hash=hash)
        await paste.set({Paste.visibility: new_visibility})

        return paste
        
    async def delete_paste(self, hash: str) -> None:
        paste = await self.get_paste(hash=hash)
        await paste.delete()

    async def delete_all_pastes(self):
        await Paste.delete_all()

    @staticmethod
    def _generate_hash(title: str, length: int = 8) -> str:
        """
        Генерация хеша на основе содержимого и временной метки
        """

        timestamp = str(datetime.now().timestamp())
        unique_string = title + timestamp + secrets.token_hex(8)
        return hashlib.sha256(unique_string.encode()).hexdigest()[:length]

