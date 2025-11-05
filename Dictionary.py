a = {
    "name": "Harshal",
    "age": 9,
    "db" : "2/5/2017",
    "Going Year": 2025,
    "std":3,
    "School": "Vetri Vikaas Public School",
    "something" : "Something"
}

print(a)
print(a["name"])
print(a.get("56"))
print(a.keys())
print(a.values())

for key,value in a.items():
    print(f"{key}: {value}")

a.update({"Friends":["Kaniyan", "Nikithan"]})
print(a)

a.pop("something")
print(a)

print(a["Friends"][0])

for i in a["Friends"]:
    print(i)