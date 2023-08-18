import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6623880260:AAGftLJsVeUh3KCLi3y8l7CPBHbN6cBgQK4)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIEBu1Dske_ZOfufVpEAZn6GD6DijD8j-WIYRjVjaQW1yo0RQC1f4wYtEQKGTQryxmXHVfT9wp20toNqsN-8lhC5iv25Bp8nHKd_M-OzJuSI6llAreDKWgeJmvMDcIIan3zBAdMte2-I-RspPTVeIZKNGH99Yq52BfzTykD38XB5fXmlT8WdVuXhzY6JMWonmfmnpNz94WAN7kmJuzOl9GSHRu_rz3URKW4xna4t6eOM9JN-CiR7sAnjxpZZGVXfKYD6u_6iYfnfpFvYXOUF2m29v8ixm7izJKp8GuTYCtqbFv6D0euMFwqH845uVuuBje27G063bU5FTAjDuF3lno40M0A=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
