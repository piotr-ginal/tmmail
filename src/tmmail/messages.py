import typing

from . import MESSAGES_ENDPOINT
from .api_entities.message import InboxMessage
from .exceptions import message as message_exceptions
from .exceptions.exceptions import UnhandledStatusCodeException
from .util.api_request import authenticated_api_request


def get_messages(jwt_token: str, *, page: int = 1) -> typing.Tuple[int, list[InboxMessage]]:
    if page < 1:
        raise message_exceptions.MessagesPageIndexException(page)

    response = authenticated_api_request(
        jwt_token,
        "GET",
        MESSAGES_ENDPOINT,
        params={"page": page},
        headers={"Accept": "application/ld+json"}
    )

    if response.status_code != 200:
        raise UnhandledStatusCodeException(
            200, response.status_code, "fetching messages"
        )

    page_messages_data = response.json()

    if len(page_messages_data["hydra:member"]) == 0:
        raise message_exceptions.MessagesPageIndexException(page)

    messages = [InboxMessage.model_validate(mes) for mes in page_messages_data["hydra:member"]]

    return int(page_messages_data["hydra:totalItems"]), messages
