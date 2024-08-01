import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def answer_questions(doc_text, questions):
    """
       Fetches answers for given questions based on the provided document text

       Args:
           doc_text (str): Text extracted from the document
           questions (list): List of questions to be answered

       Returns:
           dict: Dictionary mapping questions to their answers
       """
    answers = {}
    for question in questions:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
             {"role": "system", "content": "You are a helpful assistant."},
             {"role": "user", "content": f"Question: {question}\nAnswer based on the following text: {doc_text}"}
            ],
            max_tokens=500
        )
        answer = response.choices[0].message['content'].strip()
        if "Data Not Available" in answer or not answer:
            answers[question] = "Data Not Available"
        else:
            answers[question] = answer

    return answers
