import csv

input_file = "data/raw/payments.csv"
output_file = "data/processed/payments_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    payments = list(reader)

for payment in payments:
    payment["payment_id"] = payment["payment_id"].strip()
    payment["contract_id"] = payment["contract_id"].strip()
    payment["payment_status"] = payment["payment_status"].strip()

with open(output_file, "w", newline="") as file:
    fieldnames = [
        "payment_id",
        "contract_id",
        "payment_date",
        "payment_amount",
        "payment_status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(payments)

print("Payment data successfully transformed!")
print(f"Output file: {output_file}")