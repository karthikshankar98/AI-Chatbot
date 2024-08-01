import pytest
from utils.openai_api import answer_questions

def is_similar_answer(expected, actual):
    return expected.lower() in actual.lower() or actual.lower() in expected.lower()


def test_answer_questions():
    text = "This is a test document."
    questions = ["What is this document?"]
    answers = answer_questions(text, questions)
    assert is_similar_answer("This is a test document.", answers["What is this document?"]), "Answer extraction failed."