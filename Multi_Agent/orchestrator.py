from agents.news_fetcher import NewsFetcher
from agents.article_analyzer import ArticleAnalyzer
from agents.social_formatter import SocialFormatter


def main():
    """Orchestrates the three-agent workflow"""

    print("\n" + "=" * 60)
    print("🤖 MULTI-AGENT NEWS ANALYZER & SOCIAL POST GENERATOR")
    print("=" * 60 + "\n")

    # Get keyword from user
    keyword = input("Enter a keyword to search for news: ").strip()

    if not keyword:
        print("❌ Please enter a valid keyword.")
        return

    print(f"\n{'=' * 60}")
    print(f"🔍 AGENT 1: Fetching news about '{keyword}'...")
    print(f"{'=' * 60}\n")

    # Agent 1: Fetch article
    fetcher = NewsFetcher()
    article = fetcher.fetch_article(keyword)

    if not article:
        print("❌ No articles found. Try a different keyword.")
        return

    print(f"✅ Article Found!")
    print(f"   📰 Title: {article['title']}")
    print(f"   🏢 Source: {article['source']}")
    print(f"   🔗 URL: {article['url']}\n")

    # Agent 2: Analyze article
    print(f"{'=' * 60}")
    print("🤖 AGENT 2: Analyzing article with AI...")
    print(f"{'=' * 60}\n")

    analyzer = ArticleAnalyzer()
    analysis = analyzer.analyze(article)

    if not analysis:
        print("❌ Analysis failed. Please check your OpenAI API key and credits.")
        return

    print(f"✅ Analysis Complete!\n")
    print(f"📊 SUMMARY:")
    print(f"   {analysis['summary']}\n")
    print(f"😊 SENTIMENT: {analysis['sentiment'].upper()}\n")
    print(f"🔑 KEY POINTS:")
    for i, point in enumerate(analysis['key_points'], 1):
        print(f"   {i}. {point}")
    print()

    # Agent 3: Format social post
    print(f"{'=' * 60}")
    print("✨ AGENT 3: Generating social media post...")
    print(f"{'=' * 60}\n")

    formatter = SocialFormatter()
    post = formatter.format_post(analysis, article)

    if not post:
        print("❌ Post generation failed.")
        return

    print(f"✅ Social Media Post Generated!\n")
    print(f"{'=' * 60}")
    print(f"🐦 READY TO SHARE:")
    print(f"{'=' * 60}")
    print(f"\n{post}\n")
    print(f"{'=' * 60}")
    print(f"🔗 Source: {article['url']}")
    print(f"{'=' * 60}\n")

    print("✅ ALL AGENTS COMPLETED SUCCESSFULLY! 🎉\n")


if __name__ == "__main__":
    main()