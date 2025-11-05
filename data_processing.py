import pandas as pd

df = pd.read_csv("sales.csv")

df["Total"] =  df["quantity"] * df["price"]

grouped = df.groupby("product")["Total"].sum().reset_index()

sorted_df = grouped.sort_values(by="Total", ascending=False)
print("Sales Summary: ")
print(sorted_df)