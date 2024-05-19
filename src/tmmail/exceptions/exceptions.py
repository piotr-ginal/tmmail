import typing


class TmMailException(Exception):
    pass


class UnhandledStatusCodeException(TmMailException):

    def __init__(self, expected: str, status_code: int, when: str, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Unexpected status code: {status_code} instead of {expected} when {when}".format(
                expected=expected, status_code=status_code, when=when
            )

            super().__init__(message)


class TooManyRequestsException(TmMailException):

    def __init__(self, *, message: typing.Optional[str] = None) -> None:
        if message is None:
            message = "Too many requests"

        super().__init__(message)
