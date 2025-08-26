from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from .enums import *


class CreatePasteSchema(BaseModel):
    title: str
    text: str
    syntax: SyntaxType = SyntaxType.PYTHON
    expires_at: ExpireAt = ExpireAt.TEN_MIN
    visibility: PasteVisibility = PasteVisibility.PUBLIC

    @field_validator("title")
    @classmethod
    def vaildate_empty_string(cls, v: str):
        if not v:
            return ValueError("The titile must not be empty.")
        return v

    


class PasteSchema(CreatePasteSchema):
    hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
