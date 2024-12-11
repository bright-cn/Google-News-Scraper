## Setting Up Google News API
Follow these steps to set up the [Google News API](https://brightdata.com/products/serp-api/google-search/news).
1. **Log in to your Bright Data account.** Navigate to the **Web Scraper API** tab.
2. In the search bar, type **Google News** and select it:

   <img width="650" alt="google-news-scraper-screenshot-bright-data-web-scraper-api" src="https://github.com/user-attachments/assets/53da065a-4975-4821-9ba8-9912c9da939f">

3. Click **Start setting an API call** to start configuring your API:

   <img width="650" alt="google-news-scraper-screenshot-start-setting-api-call" src="https://github.com/user-attachments/assets/a608922c-5f2f-46f9-b687-ed62c4eeaf97">

4. Select **Get API Token** to generate a unique API token:

   <img width="650" alt="google-news-scraper-screenshot-get-api-token" src="https://github.com/user-attachments/assets/4e7f6044-dd26-43eb-b354-0726c87e83ce">

5. Click **Add token** to create a new token:

   <img width="650" alt="google-news-scraper-screenshot-add-token" src="https://github.com/user-attachments/assets/f83863c7-2174-478a-9698-ed0b23e7c962">

6. Save your API token securely - you'll need it for making API calls:

   <img width="650" alt="google-news-scraper-screenshot-new-api-token" src="https://github.com/user-attachments/assets/11d79010-94fb-41a3-9c38-3baea71aa240">

7. To find your **Dataset ID**, navigate to the **Management APIs** tab

   <img width="650" alt="google-news-scraper-screenshot-dataset-id" src="https://github.com/user-attachments/assets/d13b7901-1c66-4a13-b3f8-71b5b2bb42ad">

8. In the **Data Collection APIs** tab, use **Add inputs** to configure multiple inputs:

     <img width="650" alt="google-news-scraper-screenshot-trigger-data-collection-api" src="https://github.com/user-attachments/assets/6005a9a8-430b-448e-82f2-17c390b15155">

9. As you adjust parameters, a CURL command will generate on the right. You can:
   - Use this command to [Trigger Data Collection API](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/trigger-a-collection) directly
   - [Pass these parameters](https://github.com/triposat/Google-News-Scraper?tab=readme-ov-file#key-input-parameters) in the `_trigger_collection` function in your [code](https://github.com/triposat/Google-News-Scraper?tab=readme-ov-file#ready-to-use-python-code)
