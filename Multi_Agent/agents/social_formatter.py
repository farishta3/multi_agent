import openai
import os
from dotenv import load_dotenv

load_dotenv()


class SocialFormatter:
    """Agent 3: AI-powered social media post generator"""

    def __init__(self):
        openai.api_key = "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"

    def format_post(self, analysis, article_data):
        """Generates a social media post from the analysis."""

        if not analysis or not article_data:
            return None

        prompt = f"""
Create an engaging social media post (tweet-style, max 280 characters) based on this article analysis:

Title: {article_data['title']}
Summary: {analysis['summary']}
Sentiment: {analysis['sentiment']}
Key Points: {', '.join(analysis['key_points'])}

Requirements:
- Must be under 280 characters total
- Include 1-2 relevant emojis
- Make it engaging and shareable
- Capture the {analysis['sentiment']} sentiment
- No hashtags

Return ONLY the post text, nothing else. No quotes, no preamble.
"""

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system",
                     "content": "You are a social media expert. Return only the post text with no extra formatting or explanation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=100
            )

            post = response.choices[0].message.content.strip()

            # Remove quotes if present
            post = post.strip('"').strip("'")

            return post

        except Exception as e:
            print(f"Error formatting post: {e}")
            return None