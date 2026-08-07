import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:Anish%40123@localhost:5432/retail_db"
)

orders = pd.read_csv("data/raw/orders.csv")

orders.to_sql(
    "stg_orders",
    engine,
    if_exists="replace",
    index=False
)

print("Orders Loaded Successfully")