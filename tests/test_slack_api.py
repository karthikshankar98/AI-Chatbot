import pytest
from utils.slack_api import post_to_slack

def test_post_to_slack():
    answers = {"What is the name of the company?": "Zania"}
    post_to_slack(answers)

