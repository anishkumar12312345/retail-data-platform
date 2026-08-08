import pandas as pd

df = pd.read_csv("data/processed/orders_clean.csv")

# Basic Analytics
total_orders = len(df)
total_sales = df["amount"].sum()

print("Total Orders:", total_orders)
print("Total Sales:", total_sales)

# Product-wise sales
product_sales = df.groupby("product").agg(
    total_quantity=("quantity", "sum"),
    total_sales=("amount", "sum")
).reset_index()

print("\nProduct-wise Sales:")
print(product_sales)

# Date-wise sales
date_sales = df.groupby("order_date").agg(
    total_orders=("order_id", "count"),
    total_sales=("amount", "sum")
).reset_index()

print("\nDate-wise Sales:")
print(date_sales)

# Top selling product
top_product = (
    df.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

print("\nTop Selling Product:")
print(top_product)

# Save product analytics
product_sales.to_csv(
    "data/processed/sales_summary.csv",
    index=False
)

print("\nSales summary saved successfully!")
