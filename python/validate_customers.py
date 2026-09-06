import csv

input_file = "data/processed/customers_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

errors = []

for customer in customers:

    # Check missing customer ID
    if not customer["customer_id"].strip():
        errors.append("Missing customer_id")

    # Check missing customer name
    if not customer["customer_name"].strip():
        errors.append(
            f"{customer['customer_id']}: Missing customer_name"
        )

    # Check missing province
    if not customer["province"].strip():
        errors.append(
            f"{customer['customer_id']}: Missing province"
        )

    # Check missing city
    if not customer["city"].strip():
        errors.append(
            f"{customer['customer_id']}: Missing city"
        )

    # Check missing industry
    if not customer["industry"].strip():
        errors.append(
            f"{customer['customer_id']}: Missing industry"
        )

if errors:
    print("Data quality validation FAILED")

    for error in errors:
        print(f"- {error}")

else:
    print("Data quality validation PASSED")
    print(f"Validated {len(customers)} customer records.")