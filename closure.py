def outer(msg):
    def inner():
        return f"Message is: {msg}"
    return inner

say = outer("Vanakkam da mapla")
print(say())