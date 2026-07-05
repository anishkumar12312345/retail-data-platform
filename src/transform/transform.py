import pandas as pd

customers = pd.read_csv("data/raw/stg_customers.csv")
orders = pd.read_csv("data/raw/stg_orders.csv")
products = pd.read_csv("data/raw/stg_products.csv")
payments = pd.read_csv("data/raw/stg_payments.csv")
returns = pd.read_csv("data/raw/stg_returns.csv")

df = orders.merge(customers, on="customer_id")
df = df.merge(products, on="product_id")
df = df.merge(payments, on="order_id")
df = df.merge(returns, on="order_id", how="left")

df["reason"] = df["reason"].fillna("No Return")

df.to_csv("data/processed/final_sales.csv", index=False)

print("Transformation Completed")