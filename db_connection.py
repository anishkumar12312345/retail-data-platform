import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="retail_db",
    user="postgres",
    password="Anish@123",
    port="5432"
)

cursor = conn.cursor()

tables = [
    "stg_customers",
    "stg_products",
    "stg_orders",
    "stg_payments",
    "stg_returns"
]

for table in tables:

    cursor.execute(f"SELECT * FROM {table}")

    rows = cursor.fetchall()

    print(f"\n===== {table} =====")

    for row in rows:
        print(row)

import pandas as pd

tables = [
    "stg_customers",
    "stg_products",
    "stg_orders",
    "stg_payments",
    "stg_returns"
]

for table in tables:

    query = f"SELECT * FROM {table}"

    df = pd.read_sql(query, conn)

    df.to_csv(f"data/raw/{table}.csv", index=False)

    print(f"{table}.csv saved")
    
cursor.close()
conn.close()

print("\nDatabase Connected Successfully")