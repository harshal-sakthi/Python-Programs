name = "hArshAL"
print(name.lower())
print(name.upper())
print(name.capitalize())

mobile = "9520170502"
masked = mobile[:2] + "******" + mobile[-2:]
print(masked)

coding = "pYJs"
_ = "HarshaL s"
formatted = f"{coding.title()} - {_.title()}"
print(formatted)

product = "Iphone"
ordered_product = product.replace("Iphone", "Ipad")
print(ordered_product)

message = "Your Uber booking ID is: UB12345. Please keep it safe."
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)

promo_msg = "use zomato100 to get offer on your first order"
if "zomato100" in promo_msg:
    print("Offer Applied")
else:
    print("Offer Not Applied")

__ = "Coding: Python, JS, Java"
print("Position is: ", __.find("Python"))

n = "Harshal Sakthi"
i = " ".join([word[0].upper() for word in n.split()])
print(i)

dirty = input("Please enter with space and word or sentence: ")
clean = dirty.strip()
print(clean)

word1 = "Harshal, Kaniyan, Nikithan, Sudharshanaa_raaj, Ritik_raj, Samaran, D Sajith, Dhina"
wordcount = len(word1.split(", "))
print(wordcount)