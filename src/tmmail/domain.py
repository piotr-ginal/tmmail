from __future__ import annotations

from . import DOMAINS_ENDPOINT
from .api_entities.domain import Domain
from .api_request import api_request
from .exceptions.exceptions import UnhandledStatusCodeException

SUCCESFULL_DOMAIN_FETCH_STATUS_CODE = 200


def _get_domains(*, filter_inactive: bool = False) -> list[Domain]:
    response = api_request("GET", DOMAINS_ENDPOINT)

    if response.status_code != SUCCESFULL_DOMAIN_FETCH_STATUS_CODE:
        raise UnhandledStatusCodeException(
            SUCCESFULL_DOMAIN_FETCH_STATUS_CODE,
            response.status_code,
            f"GET request to {DOMAINS_ENDPOINT}",
        )

    domains_data = response.json()["hydra:member"]

    domains = [Domain.model_validate(dom) for dom in domains_data]

    if filter_inactive:
        domains = [dom for dom in domains if dom.is_active]

    return domains

def get_domains_active() -> list[Domain]:

    return _get_domains(filter_inactive=True)

def get_domains_all() -> list[Domain]:

    return _get_domains(filter_inactive=False)
