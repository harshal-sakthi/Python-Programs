total = 0

def total_(amount):
    global total
    total += amount
    print("I am from total(", amount, ")")

def test():
    print("I am from test(",total,")")

#total_(100)
test()