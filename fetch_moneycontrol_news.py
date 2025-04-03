# fetch_moneycontrol_news.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def fetch_moneycontrol_news(stock_name):
    """
    Scrapes the latest stock news headlines from Moneycontrol using HTML parsing.
    
    Args:
        stock_name (str): The name of the stock (e.g., "Reliance Industries")
        
    Returns:
        None: Saves the headlines in a CSV file inside the 'data' folder.
    """
    # Format stock name for URL (e.g., "Reliance Industries" -> "reliance-industries")
    formatted_name = stock_name.lower().replace(" ", "-")
    url = f"https://www.moneycontrol.com/news/business/stocks/{formatted_name}/"

    #more headers added to mimic real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",  # Do Not Track request
        "Upgrade-Insecure-Requests": "1"
    }
    
    #response = requests.get(url, headers=headers)
    session = requests.Session()
    session.headers.update(headers)

    response = session.get(url) 

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find headlines from the page (adjust the tag and class if needed)
        headlines = soup.find_all("li", class_="clearfix")
        
        news_data = []
        for item in headlines[:10]:  # Limit to first 10 headlines
            h2 = item.find("h2")
            if h2:
                headline = h2.get_text(strip=True)
                news_data.append(headline)
        
        # Ensure the 'data' folder exists
        if not os.path.exists("data"):
            os.makedirs("data")
        
        # Save the headlines to a CSV file
        df = pd.DataFrame(news_data, columns=["Headline"])
        csv_filename = f"data/{formatted_name}_news.csv"
        df.to_csv(csv_filename, index=False)
        
        print(f"✅ Scraped {len(news_data)} news articles for {stock_name}! Saved in {csv_filename}")
    else:
        print(f"❌ Failed to fetch news for {stock_name}. Status: {response.status_code}")
