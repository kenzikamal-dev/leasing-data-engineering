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
        equipment_id,
        contract_id,
        equipment_type,
        description,
        equipment_value
    FROM equipment
""")

rows = cursor.fetchall()

with open("data/raw/equipment.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "equipment_id",
        "contract_id",
        "equipment_type",
        "description",
        "equipment_value"
    ])

    writer.writerows(rows)

cursor.close()
connection.close()

print("Equipment data successfully exported to data/raw/equipment.csv")