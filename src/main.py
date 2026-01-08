import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# ---------------------------------------------------------
# IMPORT THE PROMPT LIBRARY
# ---------------------------------------------------------
# We import the dictionary 'prompt_library' from the file 'prompts.py'
try:
    from prompts import prompt_library
except ImportError:
    # Fallback if prompts.py doesn't exist yet for testing
    prompt_library = {
        "social_hype": "Write a hype social media slogan for {product_name} targeted at {target_audience}. Tone: {tone}.",
        "feature_focused": "Write a professional slogan highlighting features for {product_name} targeted at {target_audience}. Tone: {tone}."
    }

# ---------------------------------------------------------
# 1. SETUP & CONFIGURATION
# ---------------------------------------------------------
load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
# In Azure, the 'model' parameter usually requires the 'Deployment Name'
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4.1")

if not AZURE_OPENAI_API_KEY or not AZURE_OPENAI_ENDPOINT:
    raise ValueError("Azure credentials not found. Check your .env file for AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT.")

# Initialize the Azure OpenAI Client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview", # Use a stable or preview API version
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# ---------------------------------------------------------
# 2. SLOGAN GENERATOR FUNCTION
# ---------------------------------------------------------

def generate_slogans(template_key, product, audience, tone):
    """
    Generates slogans using a reusable prompt template imported from prompts.py
    """

    # Check if the key exists in our imported library
    if template_key not in prompt_library:
        return f"Error: Template '{template_key}' not found in prompts.py"

    # Load and format the prompt
    raw_template = prompt_library[template_key]

    formatted_prompt = raw_template.format(
        product_name=product,
        target_audience=audience,
        tone=tone
    )

    print(f"--- Using Deployment: {AZURE_DEPLOYMENT_NAME} ---")
    print(f"--- Loading template: {template_key} ---")

    try:
        response = client.chat.completions.create(
            model=AZURE_DEPLOYMENT_NAME, # This must match your Azure Deployment Name
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
        return f"Azure API Error: {e}"


# ---------------------------------------------------------
# 3. EXECUTION
# ---------------------------------------------------------

if __name__ == "__main__":
    # Scenario 1: Social Media
    print("SCENARIO 1: Energy Drink Launch\n")
    print(generate_slogans(
        template_key="social_hype",
        product="Bolt Energy Drink",
        audience="Gamers and Night Shift Workers",
        tone="Electric, Intense, Aggressive"
    ))

    print("\n" + "-" * 40 + "\n")

    # Scenario 2: Professional
    print("SCENARIO 2: B2B Software\n")
    print(generate_slogans(
        template_key="feature_focused",
        product="QuickBooks for Freelancers",
        audience="Small Business Owners",
        tone="Trustworthy, Professional, Calm"
    ))