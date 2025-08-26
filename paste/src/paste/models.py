from beanie import Document, Indexed
from .enums import *
from pydantic import Field
from datetime import datetime




class Paste(Document):
    hash: Indexed(str, unique=True) # type: ignore
    title: str
    text: str
    syntax: SyntaxType = SyntaxType.PYTHON
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime
    visibility: PasteVisibility = PasteVisibility.PUBLIC

    class Config:
        name = "pastes"

    @property
    def is_expired(self) -> bool:
        if self.expires_at is None:  # для NEVER
            return False
        return datetime.utcnow() > self.expires_at