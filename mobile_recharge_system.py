recharge = int(input("Please enter your recharge amount: "))
sim = input("Please enter your sim: ")
data = float(input("Please enter your balance data: "))

if recharge >=399 or data >=1 or sim == "airtel":
    print("Eligible for bonus data")
else:
    print("Not eligible for bonus data")