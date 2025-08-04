import nltk
from textblob import TextBlob

def download_nltk_data():
    """Download required NLTK data"""
    try:
        nltk.download('punkt')
        nltk.download('brown')
        print("NLTK data downloaded successfully!")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

def test_sentiment_analysis():
    """Test sentiment analysis functionality"""
    test_texts = [
        "I'm feeling really happy today!",
        "I'm so stressed and overwhelmed with work.",
        "I feel sad and lonely lately.",
        "I'm anxious about my upcoming presentation.",
        "This is a neutral statement about the weather."
    ]
    
    print("Testing sentiment analysis:")
    for text in test_texts:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        print(f"Text: {text}")
        print(f"Sentiment Score: {sentiment:.3f}")
        print(f"Classification: {'Positive' if sentiment > 0.1 else 'Negative' if sentiment < -0.1 else 'Neutral'}")
        print("-" * 50)

if __name__ == "__main__":
    download_nltk_data()
    test_sentiment_analysis()
