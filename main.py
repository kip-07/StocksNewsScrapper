# main.py

from fetch_moneycontrol_news import fetch_moneycontrol_news

def main():
    # Read stock names from stocks.txt
    try:
        with open("stocks.txt", "r") as file:
            stocks = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: stocks.txt file not found. Please create the file with stock names.")
        return
    
    # For each stock, fetch the news from Moneycontrol
    for stock in stocks:
        fetch_moneycontrol_news(stock)

if __name__ == "__main__":
    main()
from sentiment_analysis import analyze_sentiment

# Run sentiment analysis after scraping news
for stock in stocks:
    analyze_sentiment(stock)
