import csv

input_file = "data/processed/equipment_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    equipment = list(reader)

errors = []

for item in equipment:

    if not item["equipment_id"].strip():
        errors.append("Missing equipment_id")

    if not item["contract_id"].strip():
        errors.append(
            f"{item['equipment_id']}: Missing contract_id"
        )

    if not item["equipment_type"].strip():
        errors.append(
            f"{item['equipment_id']}: Missing equipment_type"
        )

    if not item["description"].strip():
        errors.append(
            f"{item['equipment_id']}: Missing description"
        )

    if not item["equipment_value"].strip():
        errors.append(
            f"{item['equipment_id']}: Missing equipment_value"
        )

if errors:
    print("Equipment data quality validation FAILED")

    for error in errors:
        print(f"- {error}")

else:
    print("Equipment data quality validation PASSED")
    print(f"Validated {len(equipment)} equipment records.")