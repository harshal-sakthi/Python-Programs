from textblob import TextBlob

print("Welcome to AI Mood Detector:")
name = input("Enter your name: ")
print(f"Nice to meet you, {name} Let us find out the sentiment of your sentence")
print("Type exit to quit\n")

while True:
    sentence = input("Enter your sentence: ")
    if sentence.lower() == "exit":
        print(f"Good Bye {name}")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Positive sentiment detected")
    elif sentiment < 0:
        print("Negative sentiment detected")
    else:
        print("Neutral sentiment detected")