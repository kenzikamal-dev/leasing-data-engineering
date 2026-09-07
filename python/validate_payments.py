import csv

input_file = "data/processed/payments_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    payments = list(reader)

errors = []

for payment in payments:

    if not payment["payment_id"].strip():
        errors.append("Missing payment_id")

    if not payment["contract_id"].strip():
        errors.append(
            f"{payment['payment_id']}: Missing contract_id"
        )

    if not payment["payment_date"].strip():
        errors.append(
            f"{payment['payment_id']}: Missing payment_date"
        )

    if not payment["payment_amount"].strip():
        errors.append(
            f"{payment['payment_id']}: Missing payment_amount"
        )

    if not payment["payment_status"].strip():
        errors.append(
            f"{payment['payment_id']}: Missing payment_status"
        )

if errors:
    print("Payment data quality validation FAILED")

    for error in errors:
        print(f"- {error}")

else:
    print("Payment data quality validation PASSED")
    print(f"Validated {len(payments)} payment records.")