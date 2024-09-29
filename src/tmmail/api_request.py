from urllib.parse import urljoin

import requests

from tmmail import BASE_API
from tmmail.exceptions import auth as auth_exceptions
from tmmail.exceptions import exceptions

TOO_MANY_REQUESTS_EXPECTED_STATUS_CODE = 429
UNAUTHORIZED_STATUS_CODE = 401


def api_request(
    method: str,
    endpoint: str,
    timeout: int = 3,
    **kwargs,  # noqa: ANN003
) -> requests.Response:
    request_url = urljoin(BASE_API, endpoint)

    response = requests.request(method, request_url, timeout=timeout, **kwargs)

    if response.status_code == TOO_MANY_REQUESTS_EXPECTED_STATUS_CODE:
        raise exceptions.TooManyRequestsException

    if response.status_code == UNAUTHORIZED_STATUS_CODE:
        raise auth_exceptions.UnauthorizedException

    return response


def authenticated_api_request(
    jwt_token: str,
    method: str,
    endpoint: str,
    timeout: int = 3,
    **kwargs,  # noqa: ANN003
) -> requests.Response:
    if "headers" not in kwargs:
        kwargs["headers"] = {}

    kwargs["headers"]["Authorization"] = f"Bearer {jwt_token}"

    return api_request(method, endpoint, timeout=timeout,**kwargs)
