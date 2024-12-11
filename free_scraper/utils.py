from typing import Optional
from dataclasses import dataclass
from urllib.parse import quote


@dataclass
class NewsItem:
    """
    Data class representing a news article with its metadata.
    """

    title: Optional[str]
    link: Optional[str]
    publication_date: Optional[str]
    source: Optional[str]
    source_url: Optional[str]
    guid: Optional[str]


class GoogleNewsScraperConfig:
    """
    Configuration settings for the Google News scraper.
    """

    def __init__(
        self,
        max_concurrent_requests: int = 5,
        output_dir: str = "google_news",
        batch_delay: float = 0.5,
    ):
        self.base_url = "https://news.google.com/rss/search?q="
        self.max_concurrent_requests = max_concurrent_requests
        self.output_dir = output_dir
        self.batch_delay = batch_delay


def get_safe_filename(term: str) -> str:
    """
    Convert search term to a safe filename.
    """
    safe_name = "".join(c if c.isalnum() else "_" for c in term.lower())
    return f"{safe_name}.json"


def create_search_url(query: str) -> str:
    """
    Create the RSS feed URL for the given search query.
    """
    return f"https://news.google.com/rss/search?q={quote(query)}"