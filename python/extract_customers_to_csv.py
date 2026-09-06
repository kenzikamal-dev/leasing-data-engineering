import mysql.connector
import csv
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

cursor.execute("""
    SELECT
        customer_id,
        customer_name,
        province,
        city,
        industry
    FROM customers
""")

rows = cursor.fetchall()

with open("data/raw/customers.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "customer_id",
        "customer_name",
        "province",
        "city",
        "industry"
    ])

    writer.writerows(rows)

cursor.close()
connection.close()

print("Customer data successfully exported to data/raw/customers.csv")