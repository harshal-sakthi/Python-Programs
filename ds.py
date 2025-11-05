order_amount = int(input("Please enter your order amount: "))
days = input("Please enter your days monday(mon), tuesday(tue), wednesday(wed), thursday(thurs), friday(fri), saturday(sat), sunday(sun)\n: ")
membership = input("Please enter your membership: ")
if (order_amount >= 1000 and days in['sat', 'sun'.lower()]) or membership == "gold".lower():
    print("Discount Applied")
else:
    print("Discount Not Applied")