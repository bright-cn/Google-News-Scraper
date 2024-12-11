## 设置 Google News API

按照以下步骤设置 [Google News API](https://bright.cn/products/serp-api/google-search/news)。

1. **登录您的 Bright Data 账户。** 然后进入 **Web Scraper API** 标签页。
2. 在搜索栏中输入 **Google News** 并选择它：

   <img width="650" alt="google-news-scraper-screenshot-bright-data-web-scraper-api" src="https://github.com/user-attachments/assets/53da065a-4975-4821-9ba8-9912c9da939f">

3. 点击 **Start setting an API call** 来开始配置您的 API：

   <img width="650" alt="google-news-scraper-screenshot-start-setting-api-call" src="https://github.com/user-attachments/assets/a608922c-5f2f-46f9-b687-ed62c4eeaf97">

4. 选择 **Get API Token** 来生成一个唯一的 API token：

   <img width="650" alt="google-news-scraper-screenshot-get-api-token" src="https://github.com/user-attachments/assets/4e7f6044-dd26-43eb-b354-0726c87e83ce">

5. 点击 **Add token** 来创建一个新的 token：

   <img width="650" alt="google-news-scraper-screenshot-add-token" src="https://github.com/user-attachments/assets/f83863c7-2174-478a-9698-ed0b23e7c962">

6. 安全地保存您的 API token —— 您需要它来进行 API 调用：

   <img width="650" alt="google-news-scraper-screenshot-new-api-token" src="https://github.com/user-attachments/assets/11d79010-94fb-41a3-9c38-3baea71aa240">

7. 要查找您的 **Dataset ID**，请前往 **Management APIs** 标签页

   <img width="650" alt="google-news-scraper-screenshot-dataset-id" src="https://github.com/user-attachments/assets/d13b7901-1c66-4a13-b3f8-71b5b2bb42ad">

8. 在 **Data Collection APIs** 标签页中，使用 **Add inputs** 来配置多个输入：

   <img width="650" alt="google-news-scraper-screenshot-trigger-data-collection-api" src="https://github.com/user-attachments/assets/6005a9a8-430b-448e-82f2-17c390b15155">

9. 当您调整参数时，右侧会生成一个 CURL 命令。您可以：
   - 使用该命令直接[触发 Data Collection API](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/trigger-a-collection)
   - 在您的[代码](https://github.com/bright-cn/Google-News-Scraper?tab=readme-ov-file#ready-to-use-python-code)中，在 `_trigger_collection` 函数中[传递这些参数](https://github.com/bright-cn/Google-News-Scraper?tab=readme-ov-file#key-input-parameters)
