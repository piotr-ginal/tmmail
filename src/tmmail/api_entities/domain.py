from .parent_entity import TmMailEntity
from pydantic import Field


class Domain(TmMailEntity):
    domain: str
    is_active: bool = Field(alias="isActive")
    is_private: bool = Field(alias="isPrivate")
