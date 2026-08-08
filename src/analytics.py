import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:Anish%40123@localhost:5432/retail_db"
)

query = """
SELECT
    SUM(amount) AS total_revenue,
    COUNT(*) AS total_orders
FROM fact_orders;
"""

df = pd.read_sql(query, engine)

print(df)

df.to_csv("data/processed/final_report.csv", index=False)

print("Report Generated Successfully!")

