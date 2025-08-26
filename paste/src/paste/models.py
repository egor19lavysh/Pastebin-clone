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
    expires_at: ExpireAt = ExpireAt.TEN_MIN
    visibility: PasteVisibility = PasteVisibility.PUBLIC

    class Config:
        name = "pastes"
