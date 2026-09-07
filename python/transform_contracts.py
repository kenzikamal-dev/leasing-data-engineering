import csv

input_file = "data/raw/contracts.csv"
output_file = "data/processed/contracts_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    contracts = list(reader)

for contract in contracts:
    contract["contract_id"] = contract["contract_id"].strip()
    contract["customer_id"] = contract["customer_id"].strip()
    contract["status"] = contract["status"].strip()

with open(output_file, "w", newline="") as file:
    fieldnames = [
        "contract_id",
        "customer_id",
        "contract_date",
        "amount_financed",
        "term_months",
        "interest_rate",
        "status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(contracts)

print("Contract data successfully transformed!")
print(f"Output file: {output_file}")