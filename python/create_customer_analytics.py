import csv
from collections import Counter

input_file = "data/processed/customers_clean.csv"
output_file = "data/analytics/customer_summary.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

province_counts = Counter(customer["province"] for customer in customers)

with open(output_file, "w", newline="") as file:
    fieldnames = ["province", "customer_count"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for province, count in province_counts.items():
        writer.writerow({
            "province": province,
            "customer_count": count
        })

print("Customer analytics dataset created!")
print(f"Output file: {output_file}")