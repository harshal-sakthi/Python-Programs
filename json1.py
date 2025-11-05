import pandas as pd

# Customers DataFrame
customers = pd.DataFrame({
    'Customer ID': [1, 2, 3],
    'Customer Name': ['John', 'Doe', 'John']
})

# Orders DataFrame (all lists same length)
orders = pd.DataFrame({
    'Order ID': [101, 202, 303, 404],
    'Customer ID': [1, 2, 1, 3],
    'Product': ["Shirt", "Pant", "Shoes", "Hat"]
})

# Inner join on 'Customer ID'
result = pd.merge(customers, orders, on='Customer ID', how='inner')

print("Inner Join:")
print(result)
