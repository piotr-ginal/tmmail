from .exceptions import TmMailException
import typing


class AuthException(TmMailException):
    pass


class InvalidCredentials(AuthException):

    def __init__(self, address: str, password: str, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Invalid credentials provided. Please check your username and password"

        self.address = address
        self.password = password

        super().__init__(message)


class UnauthorizedException(AuthException):

    def __init__(self, *, message: typing.Optional[str]) -> None:
        if message is None:
            message = "Unauthorized 401: Your token isn't correct"

        super().__init__(message)
