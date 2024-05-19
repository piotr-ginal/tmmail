from . import DOMAINS_ENDPOINT
from .api_entities.domain import Domain
from .exceptions.exceptions import UnhandledStatusCodeException
from .util.api_request import api_request


def get_domains(filter_inactive: bool = False) -> list[Domain]:
    response = api_request("GET", DOMAINS_ENDPOINT)

    if response.status_code != 200:
        raise UnhandledStatusCodeException(
            "200", response.status_code, f"GET request to {DOMAINS_ENDPOINT}"
        )

    domains_data = response.json()["hydra:member"]

    domains = [Domain.model_validate(dom) for dom in domains_data]

    if filter_inactive:
        domains = [dom for dom in domains if dom.is_active]

    return domains
