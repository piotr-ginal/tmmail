from __future__ import annotations


class TmMailException(Exception):
    pass


class UnhandledStatusCodeException(TmMailException):
    def __init__(
        self: UnhandledStatusCodeException,
        expected: int,
        status_code: int,
        when: str,
        *,
        message: str | None = None,
    ) -> None:
        if message is None:
            message = "Unexpected status code: {status_code} not {expected} when {when}"

        super().__init__(
            message.format(
                expected=expected,
                status_code=status_code,
                when=when,
            ),
        )


class TooManyRequestsException(TmMailException):
    def __init__(self: TooManyRequestsException, *, message: str | None = None) -> None:
        if message is None:
            message = "Too many requests"

        super().__init__(message)


class ConstraintViolationException(TmMailException):
    def __init__(
        self: ConstraintViolationException, message: str | None = None,
    ) -> None:
        if message is None:
            message = "Constraint violations occurred"

        super().__init__(message)
