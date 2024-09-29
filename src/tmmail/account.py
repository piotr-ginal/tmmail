from __future__ import annotations

import typing

from . import ACCCOUNTS_ENDPOINT
from .api_entities.account import Account
from .api_entities.errors import ConstraintViolation
from .api_request import api_request
from .exceptions import account as account_exceptions
from .exceptions import exceptions

if typing.TYPE_CHECKING:
    from .api_entities.domain import Domain

ACCOUNT_CREATION_EXPECTED_STATUS_CODE = 201
CONSTRAINT_VIOLATION_EXPECTED_STATUS_CODE = 422


def _handle_violations(response_data: dict) -> None:
    exception_message = "Constraint violated when attempting to create an account: "

    violated_fields: list[str] = []

    for violation in response_data["violations"]:
        violation_checked = ConstraintViolation.model_validate(violation)

        violated_fields.append(violation_checked.property_path)

        exception_message += \
            f"{violation_checked.property_path} - {violation_checked.message}"

    raise account_exceptions.CredConstraintViolationException(
        exception_message, violated_fields,
    )


def create_account(
    domain: Domain,
    username: str,
    password: str,
    *,
    violations_handler: None | typing.Callable = None,
) -> Account:
    request_json = {
        "address": f"{username}@{domain.domain}",
        "password": password,
    }

    response = api_request("POST", ACCCOUNTS_ENDPOINT, json=request_json)

    if response.status_code == ACCOUNT_CREATION_EXPECTED_STATUS_CODE:
        return Account.model_validate(response.json())

    if (
        response.status_code == CONSTRAINT_VIOLATION_EXPECTED_STATUS_CODE
        and response.json()["@type"] == "ConstraintViolationList"
    ):
        if violations_handler is None:
            violations_handler = _handle_violations

        _handle_violations(response.json())

        raise exceptions.ConstraintViolationException

    raise exceptions.UnhandledStatusCodeException(
        ACCOUNT_CREATION_EXPECTED_STATUS_CODE,
        response.status_code,
        "Encountered unhandled status code when creating an account",
    )
