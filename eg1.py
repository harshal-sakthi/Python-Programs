h = input("Enter your Feedback: ")

with open("file_log.txt", "a") as f:
    f.write(h + "\n")
print("Thanks for your Feedback!")