import subprocess
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting leasing data pipeline...")
logging.info("Pipeline started")

print("\n1. Extracting customer data...")
logging.info("Starting customer data extraction")
subprocess.run(
    ["python3", "python/extract_customers_to_csv.py"],
    check=True
)
logging.info("Customer data extraction completed")

print("\n2. Transforming customer data...")
logging.info("Starting customer data transformation")
subprocess.run(
    ["python3", "python/transform_customers.py"],
    check=True
)
logging.info("Customer data transformation completed")

print("\n3. Creating customer analytics...")
logging.info("Starting customer analytics")
subprocess.run(
    ["python3", "python/create_customer_analytics.py"],
    check=True
)
logging.info("Customer analytics completed")

print("\n4. Validating customer data...")
logging.info("Starting data quality validation")
subprocess.run(
    ["python3", "python/validate_customers.py"],
    check=True
)
logging.info("Data quality validation completed")

print("\nPipeline completed successfully!")
logging.info("Pipeline completed successfully")