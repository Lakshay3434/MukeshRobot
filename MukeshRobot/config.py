
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "29230755" # integer value, dont use ""
    API_HASH = "ab41c7247a91680d2d0dc705ad7158da"
    TOKEN = "6924632975:AAEgZTprCgNsM8NlLIYRthZHNnDuJugoaY4"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6440363814 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "Devine_Support"
    START_IMG = "https://graph.org/file/ab6e5b8f40192031e68d7.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://WAIFUGRABERBOT:WAIFUGRABERBOT@cluster0.d3razp8.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "JGGE4IGZIV2EH339"
    
    # Get your API key from https://timezonedb.com/api
    API_KEY="OGLUXI6U9XIS"

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
