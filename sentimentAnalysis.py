from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# Function to analyze sentiment
def analyze_sentiment(comment):
    # Get sentiment scores
    scores = analyzer.polarity_scores(comment)

    # Determine sentiment
    if scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, scores


# Example comment
comment = "Hello nice photos you waiting for me"
sentiment, scores = analyze_sentiment(comment)

print(f"Comment: {comment}")
print(f"Sentiment: {sentiment}")
print(f"Scores: {scores}")
