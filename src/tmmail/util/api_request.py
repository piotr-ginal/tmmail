import requests
from .. import BASE_API
from urllib.parse import urljoin
from ..exceptions import exceptions
from ..exceptions import auth as auth_exceptions


def api_request(method: str, endpoint: str, **kwargs) -> requests.Response:

    request_url = urljoin(BASE_API, endpoint)

    response = requests.request(method, request_url, **kwargs)

    if response.status_code == 429:
        raise exceptions.TooManyRequestsException()

    elif response.status_code == 401:
        raise auth_exceptions.UnauthorizedException()

    return response
