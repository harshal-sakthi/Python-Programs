age = int(input("Age: "))
has_license = input("You have licesnce or not Say yes or no: ")

if age >= 18:
    if has_license == "yes":
        print("You can drive")
    else:
        print("Go and take licesnese")
else:
    print("Your too young to drive")