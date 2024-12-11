import requests
import json
import time


class BrightDataNews:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = "gd_lnsxoxzi1omrwnka5r"

    def collect_news(self, search_queries):
        """
        Collect Google News articles using BrightData API
        """
        # 1. Trigger data collection
        print("Starting news collection...")
        trigger_response = self._trigger_collection(search_queries)
        snapshot_id = trigger_response.get("snapshot_id")
        print(f"Snapshot ID: {snapshot_id}")

        # 2. Wait for data to be ready
        print("Waiting for data...")
        while True:
            status = self._check_status(snapshot_id)
            print(f"Status: {status}")

            if status == "ready":
                # Check if data is actually available
                data = self._get_data(snapshot_id)
                if data and len(data) > 0:
                    break
            time.sleep(10)  # Wait 10 seconds before next check
        # 3. Get and save the data
        print("Saving data...")
        filename = f"news_scraper_output.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Data saved to {filename}")
        print(f"✓ Collected {len(data)} news articles")
        return data

    def _trigger_collection(self, search_queries):
        """Trigger news data collection"""
        response = requests.post(
            "https://api.brightdata.com/datasets/v3/trigger",
            headers=self.headers,
            params={"dataset_id": self.dataset_id, "include_errors": "true"},
            json=search_queries,
        )
        return response.json()

    def _check_status(self, snapshot_id):
        """Check collection status"""
        response = requests.get(
            f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}",
            headers=self.headers,
        )
        return response.json().get("status")

    def _get_data(self, snapshot_id):
        """Get collected data"""
        response = requests.get(
            f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
            headers=self.headers,
            params={"format": "json"},
        )
        return response.json()


if __name__ == "__main__":
    # Initialize with your API token
    brightdata_news = BrightDataNews("<YOUR_API_TOKEN>")

    # Define search queries
    queries = [
        {
            "url": "https://news.google.com/",
            "keyword": "chatgpt",
            "country": "US",
            "language": "en",
        },
        {
            "url": "https://news.google.com/",
            "keyword": "Politics news",
            "country": "FR",
            "language": "en",
        },
        {
            "url": "https://news.google.com/",
            "keyword": "Technology news",
            "country": "FR",
            "language": "fr",
        },
    ]

    # Collect news articles
    news_articles = brightdata_news.collect_news(queries)
