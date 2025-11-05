import pandas as pd

data = {
    "Name":["Harshal", "Kaniyan", "Nikithan"],
    "Age": [9,9,9]
}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
#print(df.Name)