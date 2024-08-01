import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")