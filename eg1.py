import pandas as pd

df = pd.read_csv("d.csv", header = None, names = ["Name", "Age", "City"])
print(df)