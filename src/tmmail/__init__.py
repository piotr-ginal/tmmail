from importlib.metadata import version

__version__ = version("tmmail")

BASE_API = "https://api.mail.tm"

ACCCOUNTS_ENDPOINT = "/accounts"
MESSAGES_ENDPOINT = "/messages"
DOMAINS_ENDPOINT = "/domains"
TOKEN_ENDPOINT = "/token"
