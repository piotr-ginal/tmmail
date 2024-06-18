from __future__ import annotations

from .exceptions import TmMailException


class MessageException(TmMailException):
    pass


class MessagesPageIndexException(MessageException):
    def __init__(
        self: MessagesPageIndexException,
        page: int,
        *,
        message: str | None = None,
    ) -> None:
        if message is None:
            message = (
                "Invalid page index: {page} is not an "
                "integer larger than 0 or page is empty"
            )

        self.page = page

        super().__init__(message.format(page=page))


class MessageNotFound(MessageException):
    def __init__(
        self: MessageNotFound, message_id: str, *, message: str | None = None,
    ) -> None:
        if message is None:
            message = "Message with id {message_id} not found"

        self.message_id = message_id

        super().__init__(message.format(message_id=message_id))
