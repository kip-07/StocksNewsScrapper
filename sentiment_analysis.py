import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import os

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(stock_name):
    file_path = f"data/{stock_name}_news.csv"
    
    if not os.path.exists(file_path):
        print(f"❌ No news file found for {stock_name}. Skipping...")
        return
    
    # Load news headlines
    df = pd.read_csv(file_path)
    
    if "Headline" not in df.columns:
        print(f"❌ No 'Headline' column in {file_path}. Skipping...")
        return

    # Apply sentiment analysis
    df["VADER_Score"] = df["Headline"].apply(lambda x: sia.polarity_scores(str(x))["compound"])
    df["Sentiment"] = df["VADER_Score"].apply(lambda x: "Positive" if x > 0.05 else "Negative" if x < -0.05 else "Neutral")
    
    df["Polarity"] = df["Headline"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df["Subjectivity"] = df["Headline"].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

    # Save processed sentiment data
    sentiment_path = f"data/{stock_name}_sentiment.csv"
    df.to_csv(sentiment_path, index=False)
    
    print(f"✅ Sentiment Analysis Completed for {stock_name}! Saved in {sentiment_path}")

# Run sentiment analysis for all stocks in stocks.txt
if __name__ == "__main__":
    with open("stocks.txt", "r") as file:
        stocks = [line.strip() for line in file if line.strip()]
    
    for stock in stocks:
        analyze_sentiment(stock)
