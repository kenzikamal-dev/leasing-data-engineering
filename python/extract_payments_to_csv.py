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
        payment_id,
        contract_id,
        payment_date,
        payment_amount,
        payment_status
    FROM payments
""")

rows = cursor.fetchall()

with open("data/raw/payments.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "payment_id",
        "contract_id",
        "payment_date",
        "payment_amount",
        "payment_status"
    ])

    writer.writerows(rows)

cursor.close()
connection.close()

print("Payment data successfully exported to data/raw/payments.csv")