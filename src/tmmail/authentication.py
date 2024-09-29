from . import TOKEN_ENDPOINT
from .api_request import api_request
from .exceptions.auth import InvalidCredentials
from .exceptions.exceptions import UnhandledStatusCodeException

SUCCESSFUL_AUTH_STATUS_CODE = 200
INVALID_CREDENTIALS_STATUS_CODE = 401

def get_auth_token(address: str, password: str) -> str:

    request_body = {
        "address": address,
        "password": password,
    }

    response = api_request("POST", TOKEN_ENDPOINT, json=request_body)

    if response.status_code == SUCCESSFUL_AUTH_STATUS_CODE:
        return response.json()["token"]

    if response.status_code == INVALID_CREDENTIALS_STATUS_CODE:
        raise InvalidCredentials(address, password)

    raise UnhandledStatusCodeException(200, response.status_code, "authenticating")
