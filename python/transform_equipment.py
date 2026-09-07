import csv

input_file = "data/raw/equipment.csv"
output_file = "data/processed/equipment_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    equipment = list(reader)

for item in equipment:
    item["equipment_id"] = item["equipment_id"].strip()
    item["contract_id"] = item["contract_id"].strip()
    item["equipment_type"] = item["equipment_type"].strip()
    item["description"] = item["description"].strip()

with open(output_file, "w", newline="") as file:
    fieldnames = [
        "equipment_id",
        "contract_id",
        "equipment_type",
        "description",
        "equipment_value"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(equipment)

print("Equipment data successfully transformed!")
print(f"Output file: {output_file}")