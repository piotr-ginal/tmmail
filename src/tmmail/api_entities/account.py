from .parent_entity import TmMailEntity


class Account(TmMailEntity):
    address: str
    quota: int
    used: int
    isDisabled: bool
    isDeleted: bool
