from beanie import Document, Indexed
from .enums import *
from pydantic import Field
from datetime import datetime




class Paste(Document):
    hash: Indexed(str, unique=True) # type: ignore
    title: str
    text: str
    syntax: SyntaxType
    created_at: datetime
    expires_at: datetime
    visibility: PasteVisibility

    class Config:
        name = "pastes"