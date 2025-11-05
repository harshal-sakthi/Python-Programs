def countdown(n):
    if n == 0:
        print("🎆🪔🧨🎆🏮🎇 Boom!")
        return
    print(n)
    countdown(n - 1)

num = int(input("Enter a number: "))
print(countdown(num))