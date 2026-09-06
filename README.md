# Leasing Data Engineering Pipeline

A portfolio Data Engineering project that demonstrates how leasing finance data can be stored in MySQL, extracted with Python, transformed into clean datasets, and prepared for analytics.

## Business Problem

Leasing companies manage large amounts of customer, contract, equipment, and payment data.

This project simulates a leasing finance data environment and demonstrates how operational data can be transformed into structured, analytics-ready datasets.

The pipeline focuses on:

* Customer information
* Leasing contracts
* Financed equipment
* Payment transactions
* Portfolio analysis

## Project Objectives

The main objectives of this project are to:

* Build a relational leasing database using MySQL
* Extract operational data using Python
* Transform and clean raw datasets
* Create analytics-ready datasets
* Apply SQL for portfolio analysis
* Build an automated ETL pipeline
* Use Git and GitHub for version control
* Apply basic data security practices

## Architecture

The project follows a simple ETL architecture:

```text
                    ┌──────────────────┐
                    │   MySQL Database │
                    │                  │
                    │ Customers        │
                    │ Contracts        │
                    │ Equipment        │
                    │ Payments         │
                    └────────┬─────────┘
                             │
                             │ Extract
                             ▼
                    ┌──────────────────┐
                    │      Python      │
                    │                  │
                    │ mysql-connector  │
                    └────────┬─────────┘
                             │
                             │ Transform
                             ▼
                    ┌──────────────────┐
                    │   Clean Dataset  │
                    │                  │
                    │ CSV / Processed  │
                    └────────┬─────────┘
                             │
                             │ Analytics
                             ▼
                    ┌──────────────────┐
                    │ Analytics Output │
                    │                  │
                    │ Customer Summary │
                    └──────────────────┘
```

### Data Flow

```text
MySQL Database
      ↓
Extract
      ↓
Raw CSV
      ↓
Transform & Clean
      ↓
Processed CSV
      ↓
Analytics
      ↓
Analytics Dataset
```

## Technologies Used

| Technology             | Purpose                                         |
| ---------------------- | ----------------------------------------------- |
| MySQL                  | Relational database and data storage            |
| SQL                    | Data analysis and portfolio queries             |
| Python                 | Data extraction, transformation, and automation |
| CSV                    | Raw and processed data exchange                 |
| mysql-connector-python | Python-to-MySQL connectivity                    |
| python-dotenv          | Environment variable management                 |
| Git                    | Version control                                 |
| GitHub                 | Source code repository and portfolio            |
| VS Code                | Development environment                         |

## Database Structure

The project uses a relational MySQL database called:

```text
leasing_data_engineering
```

The database contains four main tables.

### Customers

Stores customer information:

* Customer ID
* Customer name
* Province
* City
* Industry

### Contracts

Stores leasing contract information:

* Contract ID
* Customer ID
* Contract date
* Amount financed
* Term in months
* Interest rate
* Contract status

### Equipment

Stores information about financed equipment:

* Equipment ID
* Contract ID
* Equipment type
* Description
* Equipment value

### Payments

Stores payment transaction information:

* Payment ID
* Contract ID
* Payment date
* Payment amount
* Payment status

### Relationships

```text
Customers
    │
    │ 1-to-many
    ▼
Contracts
    │
    ├──────────────► Equipment
    │
    └──────────────► Payments
```

Primary and foreign keys are used to maintain relationships between the tables and preserve data integrity.

## Business Questions

The project uses SQL and Python to answer business questions such as:

* How many leasing contracts are in the portfolio?
* How many contracts are active?
* How much has been financed?
* How much has customers paid?
* What is the estimated outstanding balance?
* Which customers have the largest contracts?
* Which provinces have the largest leasing exposure?
* Which contracts are defaulted?
* What is the payment activity by month?

## ETL Pipeline

The project implements a Python-based ETL pipeline.

### 1. Extract

Python connects to the MySQL database and extracts customer data.

The extracted data is saved as:

```text
data/raw/customers.csv
```

### 2. Transform

The raw customer data is read and cleaned using Python.

The transformation process includes:

* Removing unnecessary whitespace
* Cleaning text fields
* Preserving the required data structure

The cleaned dataset is saved as:

```text
data/processed/customers_clean.csv
```

### 3. Analytics

The processed dataset is analyzed using Python.

A customer summary dataset is generated by province:

```text
data/analytics/customer_summary.csv
```

### 4. Pipeline Automation

The complete pipeline can be executed with:

```bash
python3 python/run_pipeline.py
```

The pipeline executes:

```text
Extract
   ↓
Transform
   ↓
Analytics
```

## SQL Analysis

SQL is used to analyze the leasing portfolio and generate business insights.

The project demonstrates:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `JOIN`
* `LEFT JOIN`
* `GROUP BY`
* `CASE`
* `SUM()`
* `COUNT()`
* `RANK()`
* `ROW_NUMBER()`
* `PARTITION BY`
* Common Table Expressions (CTEs)
* Views
* Data aggregation
* Portfolio analysis
* Payment analysis
* Default analysis

Example:

```sql
SELECT
    status,
    COUNT(*) AS contract_count,
    SUM(amount_financed) AS total_financed
FROM contracts
GROUP BY status;
```

## Python Project Structure

```text
python/
├── test_mysql_connection.py
├── extract_customers.py
├── extract_customers_to_csv.py
├── transform_customers.py
├── create_customer_analytics.py
└── run_pipeline.py
```

### Script Responsibilities

| Script                         | Responsibility                             |
| ------------------------------ | ------------------------------------------ |
| `test_mysql_connection.py`     | Tests the MySQL database connection        |
| `extract_customers.py`         | Extracts customer records from MySQL       |
| `extract_customers_to_csv.py`  | Extracts customer data and saves it as CSV |
| `transform_customers.py`       | Cleans and transforms customer data        |
| `create_customer_analytics.py` | Creates the customer analytics dataset     |
| `run_pipeline.py`              | Orchestrates the complete ETL workflow     |

## Data Structure

```text
leasing-data-engineering/
│
├── data/
│   ├── raw/
│   │   └── customers.csv
│   │
│   ├── processed/
│   │   └── customers_clean.csv
│   │
│   └── analytics/
│       └── customer_summary.csv
│
├── python/
│   ├── test_mysql_connection.py
│   ├── extract_customers.py
│   ├── extract_customers_to_csv.py
│   ├── transform_customers.py
│   ├── create_customer_analytics.py
│   └── run_pipeline.py
│
├── .gitignore
├── .env
└── README.md
```

> `.env` is intentionally excluded from GitHub and should never be committed.

## Data Security

Database credentials are not stored directly in the Python source code.

The project uses environment variables through a `.env` file:

```text
MYSQL_HOST
MYSQL_PORT
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
```

The `.env` file is excluded from Git using `.gitignore`.

This helps prevent database credentials from being accidentally committed to the GitHub repository.

The `.gitignore` file also excludes:

```text
.env
__pycache__/
*.pyc
.DS_Store
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/kenzikamal-dev/leasing-data-engineering.git
cd leasing-data-engineering
```

### 2. Configure Environment Variables

Create the `.env` file from the terminal:

```bash
cat > .env <<'EOF'
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=leasing_data_engineering
EOF
```

Replace `your_password` with your local MySQL password.

Verify the file:

```bash
ls -la .env
```

### 3. Verify Python Dependencies

Check Python:

```bash
python3 --version
```

Verify the required packages:

```bash
python3 -c "import mysql.connector; import dotenv; print('Python dependencies are installed successfully!')"
```

Expected output:

```text
Python dependencies are installed successfully!
```

### 4. Test the MySQL Connection

```bash
python3 python/test_mysql_connection.py
```

Expected output:

```text
MySQL connection successful!
```

### 5. Run the Complete ETL Pipeline

```bash
python3 python/run_pipeline.py
```

Expected final output:

```text
Pipeline completed successfully!
```

## Project Status

Current implementation includes:

* MySQL relational database
* Customer, contract, equipment, and payment data
* SQL portfolio analysis
* Python data extraction
* Data transformation
* Analytics dataset creation
* Automated ETL pipeline
* Environment-based credential management
* Git version control
* GitHub repository

## Future Improvements

Planned improvements include:

* Expand the pipeline to extract all database tables
* Add data quality validation
* Add logging and error handling
* Introduce Apache Airflow for orchestration
* Add PySpark for large-scale data processing
* Build a data warehouse model
* Add Power BI dashboards
* Add automated testing
* Containerize the pipeline with Docker
* Deploy the pipeline to a cloud environment
