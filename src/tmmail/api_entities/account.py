from pydantic import Field

from .parent_entity import TmMailEntity


class Account(TmMailEntity):
    address: str
    quota: int
    used: int
    is_disabled: bool = Field(alias="isDisabled")
    is_deleted: bool = Field(alias="isDeleted")
