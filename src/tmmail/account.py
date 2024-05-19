import typing

from .util.api_request import api_request
from .api_entities.account import Account
from .api_entities.errors import ConstraintViolation
from .api_entities.domain import Domain
from .exceptions import account as account_exceptions
from .exceptions import exceptions
from . import ACCCOUNTS_ENDPOINT


def _handle_violations(response_data: dict) -> None:
    print(response_data)

    exception_message = "Constraint violated when attempting to create an account: "

    violated_fields: list[str] = []

    for violation in response_data["violations"]:
        violation_checked = ConstraintViolation.model_validate(violation)

        violated_fields.append(violation_checked.property_path)

        exception_message += \
            f"{violation_checked.property_path} - {violation_checked.message}"

    raise account_exceptions.CredConstraintViolationException(
        exception_message, violated_fields
    )


def create_account(
    domain: Domain,
    username: str,
    password: str,
    *,
    violations_handler: typing.Optional[typing.Callable] = None
) -> Account:
    request_json = {
        "address": f"{username}@{domain.domain}",
        "password": password
    }

    response = api_request("POST", ACCCOUNTS_ENDPOINT, json=request_json)

    if response.status_code == 201:
        return Account.model_validate(response.json())

    elif response.status_code == 422 and response.json()["@type"] == "ConstraintViolationList":
        if violations_handler is None:
            violations_handler = _handle_violations

        _handle_violations(response.json())

    else:
        raise exceptions.UnhandledStatusCodeException(
            "Encountered unhandled status code when creating an account " + response.status_code
        )
