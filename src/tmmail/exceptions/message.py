import typing

from .exceptions import TmMailException


class MessageException(TmMailException):
    pass


class MessagesPageIndexException(TmMailException):

    def __init__(self, page: int, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Invalid page index: {page} is not an integer larger than 0 or page is empty"

        self.page = page

        super().__init__(message.format(page=page))
