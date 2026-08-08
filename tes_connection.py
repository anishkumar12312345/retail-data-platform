import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="retail_user",
    password="Retail@1234",
    database="retail_db"
)

print("MySQL connection successful!")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM customers")
print("Customers:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM orders")
print("Orders:", cursor.fetchone()[0])

cursor.close()
conn.close()

