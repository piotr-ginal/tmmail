import requests
from .. import BASE_API
from urllib.parse import urljoin


def api_request(method: str, endpoint: str, **kwargs) -> requests.Response:
    # TODO check endpoint

    request_url = urljoin(BASE_API, endpoint)

    response = requests.request(method, request_url, **kwargs)

    # if response.status_code in (200, 201, 204):
    return response

    # TODO status code handling
