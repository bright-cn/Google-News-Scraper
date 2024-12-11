import asyncio
import aiohttp
import json
import os
from typing import List, Dict, Tuple, Optional
from bs4 import BeautifulSoup
from dataclasses import asdict

from utils import (
    NewsItem,
    GoogleNewsScraperConfig,
    get_safe_filename,
    create_search_url,
)


class AsyncGoogleNewsScraper:
    """
    This class handles the fetching, parsing, and saving of news articles from
    Google News RSS feeds.
    """

    def __init__(self, config: Optional[GoogleNewsScraperConfig] = None):
        """Initialize the scraper with optional configuration."""
        self.config = config or GoogleNewsScraperConfig()
        self.session: Optional[aiohttp.ClientSession] = None
        self._initialize_output_directory()

    def _initialize_output_directory(self) -> None:
        """Create output directory if it doesn't exist"""
        self.config.output_dir = f"{self.config.output_dir}"
        os.makedirs(self.config.output_dir, exist_ok=True)

    async def _fetch_news(self, url: str, term: str) -> Tuple[str, str]:
        """
        Fetch RSS feed content for a given URL.
        """
        if not self.session:
            raise RuntimeError("HTTP session not initialized")
        async with self.session.get(url) as response:
            response.raise_for_status()
            content = await response.text()
            return content, term

    def _parse_rss(self, content: str) -> List[NewsItem]:
        """
        Parse RSS content and extract news items.
        """
        soup = BeautifulSoup(content, "xml")
        news_items = []

        for item in soup.find_all("item"):
            news_item = NewsItem(
                title=item.title.text if item.title else None,
                link=item.link.text if item.link else None,
                publication_date=item.pubDate.text if item.pubDate else None,
                source=item.source.text if item.source else None,
                source_url=item.source.get("url") if item.source else None,
                guid=item.guid.text if item.guid else None,
            )
            news_items.append(news_item)
        return news_items

    def _save_to_json(self, data: List[NewsItem], filename: str) -> None:
        """
        Save news items to a JSON file.
        """
        filepath = os.path.join(self.config.output_dir, filename)
        json_data = [asdict(item) for item in data]

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

    async def _process_batch(self, terms: List[str]) -> Dict[str, List[NewsItem]]:
        """
        Process a batch of search terms concurrently.
        """
        tasks = [self._fetch_news(create_search_url(term), term)
                 for term in terms]

        results = await asyncio.gather(*tasks, return_exceptions=True)
        term_results: Dict[str, List[NewsItem]] = {}

        for result, term in zip(results, terms):
            if isinstance(result, Exception):
                continue
            content, _ = result
            news_items = self._parse_rss(content)
            term_results[term] = news_items
        return term_results

    async def scrape(
        self, search_terms: List[str] | str, save_combined: bool = True
    ) -> Dict[str, List[NewsItem]]:
        """
        Scrape news for given search terms and save results.
        """
        if isinstance(search_terms, str):
            search_terms = [search_terms]
        batches = [
            search_terms[i: i + self.config.max_concurrent_requests]
            for i in range(0, len(search_terms), self.config.max_concurrent_requests)
        ]

        all_results: Dict[str, List[NewsItem]] = {}

        async with aiohttp.ClientSession() as session:
            self.session = session

            for batch in batches:
                try:
                    batch_results = await self._process_batch(batch)
                    all_results.update(batch_results)

                    # Save individual files
                    for term, news_items in batch_results.items():
                        filename = get_safe_filename(term)
                        self._save_to_json(news_items, filename)
                    await asyncio.sleep(self.config.batch_delay)
                except Exception:
                    pass
        # Save combined results
        if save_combined and all_results:
            all_news = [item for items in all_results.values()
                        for item in items]
            self._save_to_json(all_news, "combined_results.json")
        return all_results
