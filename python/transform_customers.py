import csv

input_file = "data/raw/customers.csv"
output_file = "data/processed/customers_clean.csv"

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

for customer in customers:
    customer["customer_name"] = customer["customer_name"].strip()
    customer["province"] = customer["province"].strip()
    customer["city"] = customer["city"].strip()
    customer["industry"] = customer["industry"].strip()

with open(output_file, "w", newline="") as file:
    fieldnames = [
        "customer_id",
        "customer_name",
        "province",
        "city",
        "industry"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers)

print("Customer data successfully transformed!")
print(f"Output file: {output_file}")