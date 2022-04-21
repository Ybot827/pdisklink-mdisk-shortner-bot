import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
METHOD = os.environ.get("METHOD")
PDISKLINK_API = os.environ.get("PDISKLINK_API")
MDISK_API = os.environ.get("MDISK_API")
INCLUDE_DOMAIN = os.environ.get("INCLUDE_DOMAIN")
EXCLUDE_DOMAIN = os.environ.get("EXCLUDE_DOMAIN")
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = bool(os.environ.get("FORWARD_MESSAGE"))
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
SOURCE_CODE = "Unknown"
CHANNELS = bool(os.environ.get("CHANNELS"))

