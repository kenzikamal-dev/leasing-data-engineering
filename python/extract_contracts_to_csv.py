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
        contract_id,
        customer_id,
        contract_date,
        amount_financed,
        term_months,
        interest_rate,
        status
    FROM contracts
""")

rows = cursor.fetchall()

with open("data/raw/contracts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "contract_id",
        "customer_id",
        "contract_date",
        "amount_financed",
        "term_months",
        "interest_rate",
        "status"
    ])

    writer.writerows(rows)

cursor.close()
connection.close()

print("Contract data successfully exported to data/raw/contracts.csv")