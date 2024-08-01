import sys
import json
from utils.pdf_parser import extract_text_from_pdf
from utils.openai_api import answer_questions
from utils.slack_api import post_to_slack

def main(pdf_path, questions_path):
    """
        Processes a PDF file and answers questions based on its contents

        Args:
            pdf_path (str): Path to the PDF file
            questions_path (str): Path to the JSON file containing questions

        Outputs:
            function call to slack API for posting answers on channel
        """

    text = extract_text_from_pdf(pdf_path)

    with open(questions_path, 'r') as file:
        questions = json.load(file)

    answers = answer_questions(text, questions)
    post_to_slack(answers)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_path> <questions_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    questions_path = sys.argv[2]
    main(pdf_path, questions_path)
