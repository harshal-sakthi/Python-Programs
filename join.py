import pandas as pd

customers = pd.DataFrame(
    {
        'Customer ID': [1,2,3],
        'Customer Name': ['John', 'Doe', 'John'],
    }
)

orders = pd.DataFrame({
    'Order ID': [101, 202, 303, 404],
    'Customer ID': [1, 2, 1, 3],
    'Product': ["Shirt", "Pant", "Shoes", "Hat"]
})


result = pd.merge(customers, orders, how='inner', on='Customer ID')
print("Inner Join: ")
print(result)