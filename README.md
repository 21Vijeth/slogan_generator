# Marketing Slogan Generator  
*(Prompt Engineering Assignment)*

This project demonstrates **prompt engineering** using a reusable prompt library
to generate short marketing slogans for different products.

## Features
- Reusable prompt templates with **Role, Task, and Constraints**
- Dynamic variable injection (product, audience, tone)
- Integration with an OpenAI-compatible API (OpenRouter)
- Secure API key handling using a `.env` file

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Create a .env file:
    ```bash
    OPENROUTER_API_KEY=your_api_key_here
3.  Run the script:
    ```bash
    python main.py
