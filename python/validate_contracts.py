import csv

input_file = "data/processed/contracts_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    contracts = list(reader)

errors = []

for contract in contracts:

    if not contract["contract_id"].strip():
        errors.append("Missing contract_id")

    if not contract["customer_id"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing customer_id"
        )

    if not contract["contract_date"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing contract_date"
        )

    if not contract["amount_financed"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing amount_financed"
        )

    if not contract["term_months"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing term_months"
        )

    if not contract["interest_rate"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing interest_rate"
        )

    if not contract["status"].strip():
        errors.append(
            f"{contract['contract_id']}: Missing status"
        )

if errors:
    print("Contract data quality validation FAILED")

    for error in errors:
        print(f"- {error}")

else:
    print("Contract data quality validation PASSED")
    print(f"Validated {len(contracts)} contract records.")