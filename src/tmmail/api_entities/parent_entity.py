from pydantic import BaseModel, Field
from datetime import datetime


class TmMailEntity(BaseModel):
    id: str = Field(alias="id")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
