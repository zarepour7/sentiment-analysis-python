from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "🙂 Positive"
    elif sentiment < 0:
        return "☹️ Negative"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    result = analyze_sentiment(user_input)
    print("Sentiment:", result)
