import pandas as pd

# Read raw data
df = pd.read_csv("data/raw/orders.csv")

# Basic cleaning
df = df.drop_duplicates()
df = df.dropna()

# Convert order_date to date format
df["order_date"] = pd.to_datetime(df["order_date"])

# Save processed data
df.to_csv("data/processed/orders_clean.csv", index=False)

print("Transformation successful!")
print("Rows processed:", len(df))
