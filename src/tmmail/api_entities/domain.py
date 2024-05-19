from pydantic import Field

from .parent_entity import TmMailEntity


class Domain(TmMailEntity):
    domain: str
    is_active: bool = Field(alias="isActive")
    is_private: bool = Field(alias="isPrivate")
