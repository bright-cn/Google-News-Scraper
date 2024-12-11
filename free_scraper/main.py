import asyncio
from scraper import AsyncGoogleNewsScraper
from utils import GoogleNewsScraperConfig


async def main():
    """
    Example usage of the Google News scraper.
    """
    config = GoogleNewsScraperConfig(
        max_concurrent_requests=5, output_dir="google_news_data"
    )

    scraper = AsyncGoogleNewsScraper(config)

    search_terms = [
        "chatgpt plus",
        "usa elections",
        "y combinator startups",
        "neural networks",
        "robotics",
    ]

    results = await scraper.scrape(search_terms)

    # Print summary
    print("\nScraping Summary:")
    total_articles = 0
    for term, items in results.items():
        print(f"'{term}': {len(items)} articles")
        total_articles += len(items)
    print(f"\nTotal articles found: {total_articles}")
    print(f"Results saved in: {scraper.config.output_dir}")


if __name__ == "__main__":
    asyncio.run(main())