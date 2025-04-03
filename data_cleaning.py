import os
import pandas as pd

def clean_stock_news_data():
    """Cleans scraped stock news data from CSV files in the data/ folder."""
    data_folder = "data"
    if not os.path.exists(data_folder):
        print("❌ Data folder not found!")
        return

    # Get all CSV files from the data folder
    csv_files = [f for f in os.listdir(data_folder) if f.endswith("_news.csv")]
    if not csv_files:
        print("❌ No news data found to clean.")
        return

    for file in csv_files:
        file_path = os.path.join(data_folder, file)
        try:
            df = pd.read_csv(file_path)
            
            # Remove duplicates
            df.drop_duplicates(inplace=True)
            
            # Remove empty or corrupted rows
            df.dropna(inplace=True)
            
            # Standardize text formatting
            df["Headline"] = df["Headline"].str.strip()
            df["Headline"] = df["Headline"].str.replace(r'[^\w\s]', '', regex=True)  # Remove special characters
            
            # Save cleaned data
            df.to_csv(file_path, index=False)
            print(f"✅ Cleaned and saved: {file}")
        
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

if __name__ == "__main__":
    clean_stock_news_data()
