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

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/karthikshankar98/Zania-AI-Challenge.git
   cd Zania_AI_Challenge

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
3. Change the access tokens and API keys in the .env file
   - OPENAI_API_KEY=your_openai_api_key
   - SLACK_API_TOKEN=your_slack_api_token
   - SLACK_CHANNEL_ID=your_slack_channel_id

4. Create a Slack App and set up a bot and bot tokens; Add the bot to your desired slack channel

## Usage
   ```bash
   python main.py path/to/your/document.pdf path/to/your/questions.json
   
