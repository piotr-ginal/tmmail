from . import TOKEN_ENDPOINT
from .exceptions.auth import InvalidCredentials
from .exceptions.exceptions import UnhandledStatusCodeException
from .util.api_request import api_request


def get_auth_token(address: str, password: str) -> str:

    request_body = {
        "address": address,
        "password": password
    }

    response = api_request("POST", TOKEN_ENDPOINT, json=request_body)

    if response.status_code == 200:
        return response.json()["token"]

    elif response.status_code == 401:
        raise InvalidCredentials(address, password)

    else:
        raise UnhandledStatusCodeException(200, response.status_code, "authenticating")
