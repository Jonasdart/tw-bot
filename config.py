import os
from dotenv import load_dotenv
load_dotenv()


ACCESS_TOKEN = os.get("ACCESS_TOKEN")
CHANNELS_NAME = os.get("CHANNELS_NAME", "").split(";")
COMMANDS_PREFIX = os.get("COMMANDS_PREFIX")
