def add(x):
    return x + 2
def multiply(x):
    return x * 2

def composed(x):
    return add(multiply(x))

composed = composed(2)
print(composed)