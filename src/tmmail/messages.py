import typing

from . import MESSAGES_ENDPOINT
from .api_entities.message import InboxMessageBrief, InboxMessage, InboxMessageContent
from .exceptions import message as message_exceptions
from .exceptions.exceptions import UnhandledStatusCodeException
from .util.api_request import authenticated_api_request


def get_messages(jwt_token: str, *, page: int = 1) -> typing.Tuple[int, list[InboxMessageBrief]]:
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

    messages = [InboxMessageBrief.model_validate(mes) for mes in page_messages_data["hydra:member"]]

    return int(page_messages_data["hydra:totalItems"]), messages


def get_message_content(jwt_token: str, message: typing.Union[str, InboxMessage]) -> None:

    if isinstance(message, InboxMessage):
        message: str = message.id

    endpoint = MESSAGES_ENDPOINT + f"/{message}"

    response = authenticated_api_request(jwt_token, "GET", endpoint)

    if response.status_code == 200:
        return InboxMessageContent.model_validate(response.json())
    elif response.status_code == 404:
        raise message_exceptions.MessageNotFound(message_id=message)
    else:
        raise UnhandledStatusCodeException(200, response.status_code, "fetching message content")
