import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "21016163"))
API_HASH = environ.get("API_HASH", "365f3421c4243310e1c738e2b6fb63a1")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002226136301"))
ADMINS = int(environ.get("ADMINS", "5806054139"))
DB_URI = environ.get("DB_URI", "mongodb+srv://gokumuikaioken20times:@qazplmwsxoknABC123@cluster0.4ed1fpj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
