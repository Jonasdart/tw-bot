import os
from dotenv import load_dotenv
load_dotenv()


ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
CHANNELS_NAME = os.environ.get("CHANNELS_NAME", "").split(";")
COMMANDS_PREFIX = os.environ.get("COMMANDS_PREFIX")
