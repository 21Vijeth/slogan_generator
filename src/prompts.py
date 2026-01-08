# prompts.py

"""
This file serves as the library for marketing prompt templates.
It separates the prompt content from the application logic.
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