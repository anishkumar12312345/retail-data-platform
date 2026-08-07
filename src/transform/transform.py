import pandas as pd

# Read staging files
orders = pd.read_csv("data/raw/stg_orders.csv")
customers = pd.read_csv("data/raw/stg_customers.csv")
products = pd.read_csv("data/raw/stg_products.csv")
payments = pd.read_csv("data/raw/stg_payments.csv")
returns = pd.read_csv("data/raw/stg_returns.csv")

# Merge all tables
df = orders.merge(customers, on="customer_id")
df = df.merge(products, on="product_id")
df = df.merge(payments, on="order_id")
df = df.merge(returns, on="order_id", how="left")

# Fill missing return reason
df["reason"] = df["reason"].fillna("No Return")

# Remove duplicate records
df = df.drop_duplicates()

print("Duplicate Records Removed")

# Find rejected rows
rejected = df[df.isnull().any(axis=1)]

# Save rejected rows
rejected.to_csv(
    "data/rejected/rejected_rows.csv",
    index=False
)

# Keep only valid rows
df = df.dropna()

# Save final processed data
df.to_csv(
    "data/processed/final_sales.csv",
    index=False
)

print("Transformation Completed Successfully")
print("Rejected Rows:", len(rejected))
print("Valid Rows:", len(df))

print("Total Records :", len(df))