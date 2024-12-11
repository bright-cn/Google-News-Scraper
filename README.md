# Google 新闻抓取器
本仓库提供两种从 Google 新闻收集数据的方法。  
- **免费方法：** 适用于小型项目和学习  
- **Google 新闻 API：** 适合大规模、可靠的实时数据提取

## 目录

- [方法一：免费 Google 新闻抓取器](#方法一免费-google-新闻抓取器)
  - [先决条件](#先决条件)
  - [安装](#安装)
  - [使用方法](#使用方法)
  - [输出结果](#输出结果)
- [常见抓取挑战](#常见抓取挑战)
- [方法二：Bright Data Google 新闻 API](#方法二bright-data-google-新闻-api)
  - [主要优势](#主要优势)
  - [Google 新闻 API 入门指南](#google-新闻-api-入门指南)
  - [关键输入参数](#关键输入参数)
  - [示例结果](#示例结果)
  - [可直接使用的 Python 代码](#可直接使用的-python-代码)
  - [理解 API 的实现方式](#理解-api-的实现方式)
  - [自定义您的数据收集](#自定义您的数据收集)

## 方法一：免费 Google 新闻抓取器
<img width="700" alt="image" src="https://github.com/bright-cn/Google-News-Scraper/assets/a7d34ffe-17c6-4c59-acbf-aaf84ed1b13e">

此免费工具可根据您感兴趣的任意主题收集新闻文章数据。您将获得从标题到发布日期的各种信息，并整齐地组织起来。

### 先决条件
- Python 3.9+
- 两个主要依赖包：
  - [aiohttp](https://pypi.org/project/aiohttp/)（用于发送请求）
  - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)（用于解析 HTML）

### 安装
1. 克隆此仓库：

    ```bash
    git clone https://github.com/bright-cn/Google-News-Scraper.git
    ```
2. 进入项目目录：

    ```bash
    cd Google-News-Scraper
    ```
3. 安装所需依赖项：

    ```bash
    pip install -r requirements.txt
    ```

### 使用方法
1. 前往 `free_scraper` 目录并打开 `main.py`
2. 在文件中定义您的搜索关键词：

    ```bash
    search_terms = [
        "artificial intelligence",
        "climate change",
        "space exploration",
        # 根据需要添加更多搜索词
    ]
    ```
3. 运行抓取程序：

    ```bash
    python main.py
    ```

### 输出结果
抓取器将生成 JSON 文件：  
- 针对每个搜索词的独立 JSON 文件  
- 包含所有搜索词数据的 `combined_results.json` 文件

每篇文章在 JSON 输出中包含以下内容：
```json
{
    "title": "OpenAI launches full o1 model with image uploads and analysis, debuts ChatGPT Pro - VentureBeat",
    "link": "https://news.google.com/rss/articles/CBMipgFBVV95cUxQTTVmS1I4aW1QanZXTnBfa2tBR3d0Y2JzNjJJNldBZTd1TVVfRmpxaUM3bGJld3RycXhPbU8wM1loT0JGd2JDRzFmU1pLU3FSbkRRZ0FPY29INmdhU1RsWXFqXzdLTjNCbU5ES3pIQXZLbTVmMWVhc0FqVlljeWNPOHZMeFlXV2F5Q21ac0lSZVhIOHlnS05sdkR5ZjhJTU9HazJ6MWJR?oc=5",
    "publication_date": "Thu, 05 Dec 2024 18:00:00 GMT",
    "source": "VentureBeat",
    "source_url": "https://venturebeat.com",
    "guid": "CBMipgFBVV95cUxQTTVmS1I4aW1QanZXTnBfa2tBR3d0Y2JzNjJJNldBZTd1TVVfRmpxaUM3bGJld3RycXhPbU8wM1loT0JGd2JDRzFmU1pLU3FSbkRRZ0FPY29INmdhU1RsWXFqXzdLTjNCbU5ES3pIQXZLbTVmMWVhc0FqVlljeWNPOHZMeFlXV2F5Q21ac0lSZVhIOHlnS05sdkR5ZjhJTU9HazJ6MWJR"
}
```

👉 您可以在我们的 [free_scraper/data/](https://github.com/bright-cn/Google-News-Scraper/tree/main/free_scraper/data) 目录中找到完整的示例输出。

## 常见抓取挑战
从 Google 新闻抓取数据可能相当具有挑战性。以下是您可能遇到的一些常见问题：  
1. **验证码和防机器人机制：** Google 通常会使用验证码或限速机制来阻止机器人访问其内容。  
2. **可扩展性：** 对大量数据或高频率进行抓取会让免费抓取器不堪重负。  
3. **全球和本地化新闻获取：** 为不同地区和语言定制抓取器通常需要大量的努力和人工调整。

## 方法二：Bright Data Google 新闻 API
想要更稳健的方案吗？让我们来谈谈 [Bright Data 的 Google 新闻 API](https://bright.cn/products/serp-api/google-search/news)。以下是它值得考虑的原因：

### 主要优势
- **无需基础设施烦恼：** 不用再为代理和验证码烦心
- **为扩展而生：** 在高流量下仍表现优异
- **全球覆盖：** 可获取来自任何国家、任何语言的新闻
- **隐私优先：** 符合 GDPR & CCPA 要求
- **按成功付费：** 仅对成功请求收费
- **试用再购买：** 提供 20 次免费 API 调用测试

## 开始使用 Google 新闻 API
> 如需了解设置 Google 新闻 API 的详细步骤，请查看我们的 [分步设置指南](https://github.com/bright-cn/Google-News-Scraper/blob/main/google_news_api_setup.md)。

### 关键输入参数
| **参数**      | **必需？** | **描述**                | **示例**              |
|---------------|------------|-------------------------|-----------------------|
| `url`         | 是         | 基本的 Google 新闻 URL  | `news.google.com`     |
| `keyword`     | 是         | 您的搜索主题            | `"ChatGPT"`           |
| `country`     | 否         | 获取新闻的国家          | `"US"`                |
| `language`    | 否         | 您想要的语言            | `"en"`                |

### 示例结果
以下是 API 返回的结果示例：  
```json
{
    "url": "https://www.tomsguide.com/news/live/12-days-of-openai-live-blog-chatgpt-sora",
    "title": "12 Days of OpenAI Day 2 LIVE: o1 full is here and every new ChatGPT AI announcement as it happens",
    "publisher": "Tom's Guide",
    "date": "2024-12-06T20:54:01.000Z",
    "category": null,
    "keyword": "chatgpt",
    "country": "US",
    "image": "https://news.google.com/api/attachments/CC8iK0NnNW9SbTFVTWtkNGFGSjJSVGhGVFJDb0FSaXNBaWdCTWdhQmtJcWpOQWM=-w200-h112-p-df-rw",
    "timestamp": "2024-12-08T10:06:05.122Z",
    "input": {
        "url": "https://news.google.com/",
        "keyword": "chatgpt",
        "country": "US",
        "language": "en"
    }
}
```
👉 您可以在我们的 [news_scraper_output.json](https://github.com/bright-cn/Google-News-Scraper/blob/main/google-news-api-scraper/data/news_scraper_output.json) 文件中找到完整的示例输出。

### 可直接使用的 Python 代码
下面是一个帮助您入门的脚本示例：
```python
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
```
下面是使用方法：
```python
# Initialize the client
news_client = BrightDataNews("<YOUR_API_TOKEN>")

# Define what you want to collect
queries = [
    {
        "url": "https://news.google.com/",
        "keyword": "artificial intelligence startups",
        "country": "US",
        "language": "en",
    },
    {
        "url": "https://news.google.com/",
        "keyword": "tech industry layoffs",
        "country": "US",
        "language": "en",
    },
]

# Start collection
try:
    news_data = news_client.collect_news(queries)
    print(f"Successfully collected {len(news_data)} articles")
except Exception as e:
    print(f"Collection failed: {str(e)}")
```
### 理解 API 的实现方式
1. **设置您的 API Token**
    - 首先，您需要一个 API token
    - 如果您还没有，请查看我们的[设置指南](https://github.com/bright-cn/Google-News-Scraper/blob/main/google_news_api_setup.md)
2. **开始数据采集**
    - 将搜索参数传递给 API
    - 您将获得一个 `snapshot_id`
3. **监控进度**
    - 这个过程需要几分钟
    - 我们的代码会自动检查状态：
      - "running" = 仍在收集数据
      - "ready" = 可以提取结果了！
4. **获取数据**
    - 一旦状态为 "ready"，我们就会提取并保存您的结果
    - 数据以整洁的 JSON 格式提供
    - 每篇文章都包含我们之前讨论过的所有字段

## 定制您的数据采集
您可以使用以下参数来微调您的结果：
| **参数**            | **类型**   | **描述**                                                    | **示例**                   |
|---------------------|------------|-------------------------------------------------------------|----------------------------|
| `limit`             | `integer`  | 每个输入的最大返回结果数                                    | `limit=10`                |
| `include_errors`    | `boolean`  | 获取故障报告以便进行问题排查                                | `include_errors=true`     |
| `notify`            | `url`      | 任务完成时通知的 Webhook URL                                 | `notify=https://notify-me.com/` |
| `format`            | `enum`     | 输出格式（如 JSON、NDJSON、JSONL、CSV）                     | `format=json`             |

💡 **专业提示：** 您还可以选择将数据[传送到外部存储](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview#via-deliver-to-external-storage)或通过[Webhook](https://docs.bright.cn/scraping-automation/web-data-apis/web-scraper-api/overview#via-webhook)传送。

----

需要更多细节？请查看[官方 API 文档](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview)。
