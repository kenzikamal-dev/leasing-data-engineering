import subprocess
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting leasing data pipeline...")
logging.info("Pipeline started")

try:
    print("\n1. Extracting customer data...")
    logging.info("Starting customer data extraction")

    subprocess.run(
        ["python3", "python/extract_customers_to_csv.py"],
        check=True
    )

    logging.info("Customer data extraction completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Customer data extraction failed: {error}")
    print("Customer data extraction FAILED")
    logging.error("Pipeline failed during extraction")
    raise


try:
    print("\n2. Transforming customer data...")
    logging.info("Starting customer data transformation")

    subprocess.run(
        ["python3", "python/transform_customers.py"],
        check=True
    )

    logging.info("Customer data transformation completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Customer data transformation failed: {error}")
    print("Customer data transformation FAILED")
    logging.error("Pipeline failed during transformation")
    raise


try:
    print("\n3. Creating customer analytics...")
    logging.info("Starting customer analytics")

    subprocess.run(
        ["python3", "python/create_customer_analytics.py"],
        check=True
    )

    logging.info("Customer analytics completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Customer analytics failed: {error}")
    print("Customer analytics FAILED")
    logging.error("Pipeline failed during analytics")
    raise


try:
    print("\n4. Validating customer data...")
    logging.info("Starting data quality validation")

    subprocess.run(
        ["python3", "python/validate_customers.py"],
        check=True
    )

    logging.info("Data quality validation completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Data quality validation failed: {error}")
    print("Data quality validation FAILED")
    logging.error("Pipeline failed during data validation")
    raise


print("\nPipeline completed successfully!")
logging.info("Pipeline completed successfully")