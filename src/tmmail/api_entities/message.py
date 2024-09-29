from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from .parent_entity import TmMailEntity


class MailContact(BaseModel):
    name: str
    address: EmailStr


class InboxMessage(TmMailEntity):
    account_id: str = Field(alias="accountId", repr=False)
    message_id: str = Field(alias="msgid", repr=False)
    sender: MailContact = Field(alias="from")
    recipients: list[MailContact] = Field(alias="to", repr=False)
    subject: str
    intro: str = Field(repr=False)
    seen: bool = Field(repr=False)
    is_deleted: bool = Field(alias="isDeleted", repr=False)
    has_attachments: bool = Field(alias="hasAttachments")
    size: int = Field(repr=False, ge=0)
    download_url: str = Field(alias="downloadUrl", repr=False)


class InboxMessageBrief(InboxMessage):
    pass


class InboxMessageContent(InboxMessage):
    cc: list[str] = Field(repr=False)
    bcc: list[str] = Field(repr=False)
    flagged: bool = Field(repr=False)
    retention: bool = Field(repr=False)
    retention_date: datetime = Field(alias="retentionDate", repr=False)
    text: str
    html: list[str] = Field(repr=False)
    source_url: str = Field(alias="sourceUrl", repr=False)
