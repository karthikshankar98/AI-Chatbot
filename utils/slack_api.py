from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from config import SLACK_API_TOKEN, SLACK_CHANNEL_ID

client = WebClient(token=SLACK_API_TOKEN)

def post_to_slack(answers):
    """
        This function posts the chatbot's answers on a slack channel

    Args:
        answers (str): Answers to queries by the chatbot

    Outputs:
        str: Answers posted on a slack channel

    """

    message = "Here are the answers extracted from the PDF:\n"
    for question, answer in answers.items():
        message += f"*{question}*\n{answer}\n\n"

    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=message
        )
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")