import requests
from .. import BASE_API
from urllib.parse import urljoin
from ..exceptions import exceptions


def api_request(method: str, endpoint: str, **kwargs) -> requests.Response:

    request_url = urljoin(BASE_API, endpoint)

    response = requests.request(method, request_url, **kwargs)

    if response.status_code == 429:
        raise exceptions.TooManyRequestsException()

    return response
