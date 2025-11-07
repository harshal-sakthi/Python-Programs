import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Sentiment Spy{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}")
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.CYAN}Welcome, {user_name}!{Style.RESET_ALL}")
print("Type a sentence and I’ll analyze its sentiment using TextBlob.")
print(f"{Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'exit'{Style.RESET_ALL} to quit.\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.BLUE}Please enter a valid sentence.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.BLUE}History cleared.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} ({sentiment_type}, Polarity: {polarity:.2f}){Style.RESET_ALL}")
        continue

    # Sentiment analysis
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected! (Polarity: {polarity:.2f}){Style.RESET_ALL}")
