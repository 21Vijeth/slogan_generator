import os
from openai import OpenAI
from dotenv import load_dotenv

# ---------------------------------------------------------
# 1. SETUP & CONFIGURATION
# ---------------------------------------------------------

"""
Marketing Slogan Generator
Demonstrates reusable prompt templates and prompt engineering
using an OpenAI-compatible API (OpenRouter).
"""

# Load environment variables from .env file
load_dotenv()

# Read API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found. Check your .env file.")

# Initialize OpenAI client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# Choose any OpenRouter-supported model
MODEL_NAME = "openai/gpt-4o-mini"

# ---------------------------------------------------------
# 2. PROMPT LIBRARY (Reusable Templates)
# ---------------------------------------------------------

"""
prompt_library:
Reusable prompt templates defining:
- Role
- Task
- Context
- Constraints
"""

prompt_library = {
    "feature_focused": """
Role: You are a Senior Product Copywriter.
Task: Write 3 punchy marketing slogans for the product described below.

Context:
- Product: {product_name}
- Audience: {target_audience}
- Tone: {tone}

Constraints:
- Max 10 words per slogan.
- Focus on utility and problem-solving.
- No fluff, jargon, or exaggerated claims.
- Format as a numbered list.
""",

    "social_hype": """
Role: You are a Gen-Z Social Media Influencer.
Task: Create 3 viral captions or slogans for the product described below.

Context:
- Product: {product_name}
- Audience: {target_audience}
- Tone: {tone}

Constraints:
- Use relevant emojis.
- High energy and excitement.
- No false or misleading claims.
- Must be under 280 characters.
- Format as a numbered list.
"""
}

# ---------------------------------------------------------
# 3. SLOGAN GENERATOR FUNCTION
# ---------------------------------------------------------

def generate_slogans(template_key, product, audience, tone):
    """
    Generates slogans using a reusable prompt template.
    """

    if template_key not in prompt_library:
        return "Error: Template not found."

    formatted_prompt = prompt_library[template_key].format(
        product_name=product,
        target_audience=audience,
        tone=tone
    )

    print(f"--- Using model: {MODEL_NAME} ---")

    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://localhost:3000",
                "X-Title": "Prompt Library Assignment",
            },
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that follows instructions strictly."
                },
                {
                    "role": "user",
                    "content": formatted_prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"API Error: {e}"

# ---------------------------------------------------------
# 4. EXECUTION (Testing)
# ---------------------------------------------------------

print("SCENARIO 1: Energy Drink Launch\n")
print(generate_slogans(
    template_key="social_hype",
    product="Bolt Energy Drink",
    audience="Gamers and Night Shift Workers",
    tone="Electric, Intense, Aggressive"
))

print("\n" + "-" * 40 + "\n")

print("SCENARIO 2: B2B Software\n")
print(generate_slogans(
    template_key="feature_focused",
    product="QuickBooks for Freelancers",
    audience="Small Business Owners",
    tone="Trustworthy, Professional, Calm"
))
