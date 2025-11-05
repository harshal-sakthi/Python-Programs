items = []

while True:
    item = input("Enter items: ")

    if item.lower() == "done":
        break
    items.append(item)
print(f"Items in Cart: {items}")