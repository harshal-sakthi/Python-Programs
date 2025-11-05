import matplotlib.pyplot as plt
import csv

months = []
sales = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        months.append(row["Month"])
        sales.append(int(row["Sales"]))


plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
#plt.savefig("Monthly Sales Report.png")
plt.show()