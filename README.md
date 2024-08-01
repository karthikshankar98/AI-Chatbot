# Zania-AI-Challenge

This project contains the implementation of an AI agent that leverages the capabilities of a large language model (LLM) to extract answers from a PDF document and post the results on Slack.

## Features
- PDF text extraction
- Question answering using OpenAI's GPT-4o-mini model
- Posting results to Slack
- High-quality, production-grade code

## Requirements
- Python 3.7+
- Required Python packages (see `requirements.txt`)

## File/Directory Descriptions
- main.py: The main entry point for the application. It processes the PDF file and questions, retrieves answers using the OpenAI API, and posts the results to a Slack channel
- requirements.txt: Lists all the dependencies required for the project, making it easy to install them using 'pip'
- config.py: Contains configuration settings, such as API keys and other constants, which are used throughout the project
- .env: Contains API keys and Access tokens

  utils
- utils/init.py: An empty file that marks the utils directory as a Python package
- utils/pdf_parser.py: Contains functions for extracting text from PDF files
- utils/openai_api.py: Implements the logic for interacting with the OpenAI API to generate answers based on the extracted text and questions
- utils/slack_api.py: Contains functions for posting messages to a Slack channel using the Slack API

  tests
- tests/init.py: An empty file that marks the tests directory as a Python package
- tests/test_pdf_parser.py: In future, will contain additional unit tests for the PDF parsing functionality
- tests/test_openai_api.py: In future, will contain additional unit tests for the OpenAI API interaction functionality
- tests/test_slack_api.py: In future, will contain additional unit tests for the Slack API interaction functionality

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/karthikshankar98/Zania-AI-Challenge.git
   cd Zania_AI_Challenge
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Change the access tokens and API keys in the .env file
   - OPENAI_API_KEY=your_openai_api_key
   - SLACK_API_TOKEN=your_slack_api_token
   - SLACK_CHANNEL_ID=your_slack_channel_id

4. Create a Slack App and set up a bot and bot tokens; Add the bot to your desired Slack channel

## Usage
   Execute main.py file as shown below to see the chatbot responses on a Slack channel
   ```bash
   python main.py path/to/your/document.pdf path/to/your/questions.json
   ```
## Future Improvements for Stable Production release
- Optimize Slack message formatting
- Include more comprehensive unit tests
- Additional error handling
