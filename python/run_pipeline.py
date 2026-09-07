import subprocess
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting leasing data pipeline...")
logging.info("Pipeline started")


# ============================================================
# 1. EXTRACT DATA
# ============================================================

try:
    print("\n1. Extracting customer data...")
    logging.info("Starting customer data extraction")

    subprocess.run(
        ["python3", "python/extract_customers_to_csv.py"],
        check=True
    )

    logging.info("Customer data extraction completed")

    print("\n1.1 Extracting contract data...")
    logging.info("Starting contract data extraction")

    subprocess.run(
        ["python3", "python/extract_contracts_to_csv.py"],
        check=True
    )

    logging.info("Contract data extraction completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Data extraction failed: {error}")
    print("Data extraction FAILED")
    logging.error("Pipeline failed during extraction")
    raise


# ============================================================
# 2. TRANSFORM DATA
# ============================================================

try:
    print("\n2. Transforming customer data...")
    logging.info("Starting customer data transformation")

    subprocess.run(
        ["python3", "python/transform_customers.py"],
        check=True
    )

    logging.info("Customer data transformation completed")

    print("\n2.1 Transforming contract data...")
    logging.info("Starting contract data transformation")

    subprocess.run(
        ["python3", "python/transform_contracts.py"],
        check=True
    )

    logging.info("Contract data transformation completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Data transformation failed: {error}")
    print("Data transformation FAILED")
    logging.error("Pipeline failed during transformation")
    raise


# ============================================================
# 3. CREATE ANALYTICS
# ============================================================

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


# ============================================================
# 4. DATA QUALITY VALIDATION
# ============================================================

try:
    print("\n4. Validating customer data...")
    logging.info("Starting customer data quality validation")

    subprocess.run(
        ["python3", "python/validate_customers.py"],
        check=True
    )

    logging.info("Customer data quality validation completed")

except subprocess.CalledProcessError as error:
    logging.error(f"Customer data validation failed: {error}")
    print("Customer data validation FAILED")
    logging.error("Pipeline failed during data validation")
    raise


# ============================================================
# PIPELINE COMPLETE
# ============================================================

print("\nPipeline completed successfully!")
logging.info("Pipeline completed successfully")