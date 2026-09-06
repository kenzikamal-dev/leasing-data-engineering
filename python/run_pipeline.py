import subprocess

print("Starting leasing data pipeline...")

print("\n1. Extracting customer data...")
subprocess.run(["python3", "python/extract_customers_to_csv.py"], check=True)

print("\n2. Transforming customer data...")
subprocess.run(["python3", "python/transform_customers.py"], check=True)

print("\n3. Creating customer analytics...")
subprocess.run(["python3", "python/create_customer_analytics.py"], check=True)

print("\n4. Validating customer data...")
subprocess.run(["python3", "python/validate_customers.py"], check=True)

print("\nPipeline completed successfully!")