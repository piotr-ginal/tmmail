from __future__ import annotations

from tmmail.api_entities.message import (
    InboxMessage,
    InboxMessageBrief,
    InboxMessageContent,
)
from tmmail.api_request import authenticated_api_request
from tmmail.exceptions import message as message_exceptions
from tmmail.exceptions.exceptions import UnhandledStatusCodeException

from . import MESSAGES_ENDPOINT

SUCCESFUL_MESSAGE_FETCH_STATUS_CODE = 200
SUCCESFUL_MESSAGE_CONTENT_FETCH_STATUS_CODE = 200


def get_messages(
    jwt_token: str,
    *,
    page: int = 1,
) -> tuple[int, list[InboxMessageBrief]]:
    if page < 1:
        raise message_exceptions.MessagesPageIndexException(page)

    response = authenticated_api_request(
        jwt_token,
        "GET",
        MESSAGES_ENDPOINT,
        params={"page": page},
        headers={"Accept": "application/ld+json"},
    )

    if response.status_code != SUCCESFUL_MESSAGE_FETCH_STATUS_CODE:
        raise UnhandledStatusCodeException(
            SUCCESFUL_MESSAGE_FETCH_STATUS_CODE,
            response.status_code,
            "fetching messages",
        )

    page_messages_data = response.json()

    if len(page_messages_data["hydra:member"]) == 0:
        raise message_exceptions.MessagesPageIndexException(page)

    messages = [
        InboxMessageBrief.model_validate(mes)
        for mes in page_messages_data["hydra:member"]
    ]

    return int(page_messages_data["hydra:totalItems"]), messages


def get_message_content(
    jwt_token: str, message: str | InboxMessage,
) -> InboxMessageContent:
    if isinstance(message, InboxMessage):
        message = message.id

    endpoint = MESSAGES_ENDPOINT + f"/{message}"

    response = authenticated_api_request(jwt_token, "GET", endpoint)

    if response.status_code == SUCCESFUL_MESSAGE_CONTENT_FETCH_STATUS_CODE:
        return InboxMessageContent.model_validate(response.json())

    if response.status_code == SUCCESFUL_MESSAGE_CONTENT_FETCH_STATUS_CODE:
        raise message_exceptions.MessageNotFound(message_id=message)

    raise UnhandledStatusCodeException(
        SUCCESFUL_MESSAGE_CONTENT_FETCH_STATUS_CODE,
        response.status_code,
        "fetching message content",
    )
