Coding = ["Python", "Javascript", "Java", "Go", "TypeScript", "Robomind", "PHP", "C++", "C#"]
print(Coding)

for _ in Coding:
    print("Coding:", _)

#chek if
if "Python" in Coding:
    print("_")
else:
    print("__")

#Replace
Coding[5] = "C"
print(Coding)


#Enumarate

for i,j in enumerate(Coding):
    print(f"Location: {i}, Value: {j}")