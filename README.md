# Stock News Scraper

## 📌 Project Overview
Stock News Scraper is a Python-based web scraping tool that fetches the latest stock-related news from **Moneycontrol** and performs **sentiment analysis** on the news articles. The project also includes **data cleaning, word frequency analysis, and visualization** of stock-related trends.


## 🚀 Features
- **Web Scraping:** Fetches stock news from Moneycontrol using `BeautifulSoup`.
- **Data Cleaning:** Removes unwanted characters, duplicates, and noise from scraped data.
- **Sentiment Analysis:** Uses `NLTK` to analyze positive, negative, or neutral sentiments.
- **Word Frequency Analysis:** Generates a word cloud and frequency distribution of stock-related keyword


## 📂 Project Structure
```
StockNewsScraper/
│-- data/                    # Folder for storing scraped data and sentiment analysis results
│   │-- reliance_news.csv
│   │-- tcs_news.csv
│   │-- ...
│-- .ipynb_checkpoints/      # Jupyter Notebook checkpoints (Git ignored)
│-- fetch_moneycontrol_news.py  # Web scraping script
│-- data_cleaning.py         # Cleans scraped news data
│-- sentiment_analysis.py    # Sentiment analysis on news articles
│-- stocks.txt               # List of stock names to fetch news for
│-- main.py                  # Main script to run the pipeline
│-- README.md                # Project documentation (this file)
│-- requirements.txt         # Dependencies for easy setup
```


## 📊 Results & Analysis
- All scraped data is stored in `data/`.
- Sentiment analysis results are saved as CSV files for each stock.
- Word frequency and visualizations provide insights into stock-related news trends.


