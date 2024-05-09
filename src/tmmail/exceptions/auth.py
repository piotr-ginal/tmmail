from .exceptions import TmMailException


class AuthException(TmMailException):
    pass


class InvalidCredentials(AuthException):
    pass
