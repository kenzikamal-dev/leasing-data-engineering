# Leasing Data Engineering Project

## Business Problem

ABC Leasing Finance needs a reliable data system to organize
customer, leasing contract, equipment, and payment data.

The company wants to use this data to understand its leasing
portfolio and answer important business questions.

## Project Objective

Build a leasing finance data pipeline that stores, cleans,
transforms, and prepares data for analytics.

## Main Business Entities

- Customer
- Leasing Contract
- Equipment
- Payment

## Data Entities and Attributes

### Customer

- customer_id
- customer_name
- province
- city
- industry

### Contract

- contract_id
- customer_id
- contract_date
- amount_financed
- term_months
- interest_rate
- status

### Equipment

- equipment_id
- contract_id
- equipment_type
- description
- equipment_value

### Payment

- payment_id
- contract_id
- payment_date
- payment_amount
- payment_status

## Keys and Relationships

### Primary Keys

- customers.customer_id
- contracts.contract_id
- equipment.equipment_id
- payments.payment_id

### Foreign Keys

- contracts.customer_id → customers.customer_id
- equipment.contract_id → contracts.contract_id
- payments.contract_id → contracts.contract_id



## Business Questions

- How many leasing contracts do we have?
- How many contracts are active?
- How much equipment has been financed?
- How much has customers paid?
- What is the outstanding balance?
- Which customers have the largest contracts?
- Which province has the largest leasing portfolio?

## Sample Data Scope

### Customers

Business customers from different industries:

- Construction
- Transportation
- Technology
- Healthcare
- Manufacturing

### Contracts

Leasing contracts with:

- Contract date
- Amount financed
- Term
- Interest rate
- Status

Possible statuses:

- Active
- Paid Off
- Defaulted

### Equipment

Examples:

- Excavator
- Forklift
- Delivery Truck
- Server
- Medical Equipment
- Manufacturing Machine

### Payments

Each leasing contract can have multiple payments.

Payment information includes:

- Payment date
- Payment amount
- Payment status

### Provinces

- Ontario
- Quebec
- Alberta
- British Columbia

## Database Tables

### customers

Stores information about leasing customers.

### contracts

| Column | Data Type | Key | Description |
|---|---|---|---|
| contract_id | VARCHAR(10) | PK | Unique leasing contract identifier |
| customer_id | VARCHAR(10) | FK | Customer associated with the contract |
| contract_date | DATE | | Contract start date |
| amount_financed | DECIMAL(12,2) | | Amount financed |
| term_months | INT | | Contract term in months |
| interest_rate | DECIMAL(5,2) | | Annual interest rate (%) |
| status | VARCHAR(20) | | Contract status |

### contracts

Stores information about leasing contracts.

### equipment

Stores information about financed equipment.

### equipment

| Column | Data Type | Key | Description |
|---|---|---|---|
| equipment_id | VARCHAR(10) | PK | Unique equipment identifier |
| contract_id | VARCHAR(10) | FK | Contract financing the equipment |
| equipment_type | VARCHAR(50) | | Equipment category |
| description | VARCHAR(100) | | Equipment description |
| equipment_value | DECIMAL(12,2) | | Value of the equipment |

### payments

Stores information about customer payments.

### payments

| Column | Data Type | Key | Description |
|---|---|---|---|
| payment_id | VARCHAR(10) | PK | Unique payment identifier |
| contract_id | VARCHAR(10) | FK | Contract associated with the payment |
| payment_date | DATE | | Date payment was made |
| payment_amount | DECIMAL(12,2) | | Payment amount |
| payment_status | VARCHAR(20) | | Payment status |

## Table Design

### customers

| Column | Data Type | Key | Description |
|---|---|---|---|
| customer_id | VARCHAR(10) | PK | Unique customer identifier |
| customer_name | VARCHAR(100) | | Customer/company name |
| province | VARCHAR(50) | | Customer province |
| city | VARCHAR(50) | | Customer city |
| industry | VARCHAR(50) | | Customer industry |