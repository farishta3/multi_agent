import unittest
from unittest.mock import patch, MagicMock
from agents.news_fetcher import NewsFetcher
from agents.article_analyzer import ArticleAnalyzer
from agents.social_formatter import SocialFormatter


class TestNewsFetcher(unittest.TestCase):
    """Test cases for Agent 1: News Fetcher"""

    @patch('agents.news_fetcher.requests.get')
    def test_fetch_article_success(self, mock_get):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'articles': [{
                'title': 'Test Article',
                'content': 'Test content',
                'url': 'https://test.com',
                'source': {'name': 'Test Source'}
            }]
        }
        mock_get.return_value = mock_response

        fetcher = NewsFetcher()
        result = fetcher.fetch_article('test')

        self.assertIsNotNone(result)
        self.assertEqual(result['title'], 'Test Article')

    @patch('agents.news_fetcher.requests.get')
    def test_fetch_article_no_results(self, mock_get):
        # Mock empty response
        mock_response = MagicMock()
        mock_response.json.return_value = {'articles': []}
        mock_get.return_value = mock_response

        fetcher = NewsFetcher()
        result = fetcher.fetch_article('nonexistent')

        self.assertIsNone(result)


class TestArticleAnalyzer(unittest.TestCase):
    """Test cases for Agent 2: Article Analyzer"""

    def test_analyze_with_none_input(self):
        analyzer = ArticleAnalyzer()
        result = analyzer.analyze(None)
        self.assertIsNone(result)


class TestSocialFormatter(unittest.TestCase):
    """Test cases for Agent 3: Social Formatter"""

    def test_format_post_with_none_input(self):
        formatter = SocialFormatter()
        result = formatter.format_post(None, None)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()