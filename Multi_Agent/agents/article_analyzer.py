import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()


class ArticleAnalyzer:
    """Agent 2: AI-powered article analyzer using GPT"""

    def __init__(self):
        openai.api_key = "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"

    def analyze(self, article_data):
        """Analyzes article using GPT to extract summary, key points, and sentiment."""

        if not article_data:
            return None

        prompt = f"""
Analyze this news article and provide:
1. A brief summary (2-3 sentences)
2. 3-5 key points as a list
3. Overall sentiment (positive/negative/neutral)

Article Title: {article_data['title']}
Article Content: {article_data['content']}

Return ONLY valid JSON in this exact format with no additional text:
{{
  "summary": "your summary here",
  "key_points": ["point1", "point2", "point3"],
  "sentiment": "positive"
}}
"""

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system",
                     "content": "You are a professional news analyst. Always return valid JSON only, no markdown or extra text."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            result = response.choices[0].message.content.strip()

            # Remove markdown code blocks if present
            if result.startswith('```'):
                result = result.split('```')[1]
                if result.startswith('json'):
                    result = result[4:]

            # Parse JSON response
            analysis = json.loads(result.strip())
            return analysis

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Raw response: {result}")
            return None
        except Exception as e:
            print(f"Error analyzing article: {e}")
            return None