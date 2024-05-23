import typing

from .exceptions import TmMailException


class MessageException(TmMailException):
    pass


class MessagesPageIndexException(MessageException):

    def __init__(self, page: int, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Invalid page index: {page} is not an integer larger than 0 or page is empty"

        self.page = page

        super().__init__(message.format(page=page))


class MessageNotFound(MessageException):

    def __init__(self, message_id: str, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Message with id {message_id} not found"

        self.message_id = message_id

        super().__init__(message.format(message_id=message_id))
