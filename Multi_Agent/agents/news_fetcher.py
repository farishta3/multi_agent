import requests
import os
from dotenv import load_dotenv

load_dotenv()


class NewsFetcher:
    """Agent 1: Fetches news articles from NewsAPI (Non-AI Agent)"""

    def __init__(self):
        self.api_key = os.getenv('NEWS_API_KEY')
        self.base_url = 'https://newsapi.org/v2/everything'

    def fetch_article(self, keyword):
        """Fetches the latest news article for a given keyword."""
        params = {
            'q': keyword,
            'apiKey': self.api_key,
            'sortBy': 'publishedAt',
            'pageSize': 1,
            'language': 'en'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data['articles']:
                article = data['articles'][0]
                return {
                    'title': article['title'],
                    'content': article['content'] or article['description'],
                    'url': article['url'],
                    'source': article['source']['name']
                }
            else:
                print("No articles found for this keyword.")
                return None

        except Exception as e:
            print(f"Error fetching article: {e}")
            return None