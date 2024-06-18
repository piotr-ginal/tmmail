from __future__ import annotations

from .exceptions import TmMailException


class AccountCreationException(TmMailException):
    pass


class CredConstraintViolationException(AccountCreationException):
    def __init__(
        self: CredConstraintViolationException,
        message: str,
        violated_fields: list[str],
    ) -> None:
        super().__init__(message)

        self.violated_fields = violated_fields
