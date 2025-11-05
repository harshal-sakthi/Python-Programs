Coding = ["Python", "Javascript", "Java", "Go", "TypeScript", "Robomind", "PHP", "C++", "C#"]
print(Coding)

#List methods
Coding.append("Rust")
print(f"After Append: {Coding}")

Coding.insert(6, "Ruby")
print(f"After Insert: {Coding}")

Coding.remove("Robomind")
print(f"After Remove: {Coding}")

Coding.pop()
print(f"After Pop: {Coding}")

Coding.reverse()
print(f"After Reverse: {Coding}")

print("Count: ", Coding.count('Java'))

print("Index of Python: ", Coding.index('Python'))
