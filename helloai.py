print("Hi I am Hello AI bot")
name=input("What is your name? ")

print(f"Nice to meet you {name}")
print("How was you day good/bad: ")
mood=input().lower()

if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print("Hope! things get better soon")
else:
    print("Sometimes its hard to put feeling in words")