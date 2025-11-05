def get_numbers(n):
    for i in range(n):
        yield i
a = int(input("Enter a number: "))
for num in get_numbers(a):
    print(num)