import pandas as pd

orders = pd.read_csv("data/raw/orders.csv")
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
payments = pd.read_csv("data/raw/payments.csv")
returns = pd.read_csv("data/raw/returns.csv")

print(orders.head())