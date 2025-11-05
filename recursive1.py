def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
inputa = int(input("Enter a number: "))
print(factorial(inputa))