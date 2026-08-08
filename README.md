# Retail Data Platform - Daily Progress

## Project Overview
This project is an End-to-End Retail Data Platform ETL Pipeline built using Python, PostgreSQL, SQLAlchemy, Pandas, and Git.

---

## Day 1
- Created project folder structure.
- Initialized Git repository.
- Created Python virtual environment.
- Installed required libraries.

---

## Day 2
- Connected Python with PostgreSQL.
- Created database.
- Tested database connection.

---

## Day 3
- Added raw retail CSV data.
- Extracted data using Pandas.
- Displayed dataset successfully.

---

## Day 4
- Performed data quality checks.
- Identified missing values.
- Separated rejected records.

---

## Day 5
- Applied data transformation.
- Cleaned dataset.
- Generated processed CSV file.

---

## Day 6
- Loaded processed data into PostgreSQL.
- Created staging tables.
- Verified inserted records.

---

## Day 7
- Created Customer Dimension table.
- Loaded customer data.

---

## Day 8
- Created Product Dimension table.
- Loaded product data.

---

## Day 9
- Created Fact Orders table.
- Loaded order records.

---

## Day 10
- Completed ETL Pipeline.
- Validated all database tables.

---

## Day 11
- Wrote SQL scripts for analytics.
- Generated revenue and order reports.

---

## Day 12
- Created analytics.py.
- Connected Python with PostgreSQL.
- Exported analytics report to CSV.

---

## Day 13
- Organized project folders.
- Updated project structure.
- Cleaned unnecessary files.

---

## Day 14
- Uploaded complete project to GitHub.
- Added SQL scripts and analytics files.
- Verified repository.

---

## Day 15
- Updated README.md.
- Added project documentation.
- Final project review completed.

---

## Technologies Used
- Python
- PostgreSQL
- Pandas
- SQLAlchemy
- Git & GitHub

## Author
**Anish Kumar**

## Power BI Dashboard

### KPIs
- Total Revenue
- Total Orders
- Total Customers
- Average Order Value

### Charts
- Product Wise Sales
- Sales by Customer
- Product Distribution (Donut Chart)
- Year Wise Sales

### Filters
- Customer Name
- Product Name# Retail Data Platform

A data engineering project that demonstrates an end-to-end retail data pipeline using Python, Apache Airflow, data transformation, analytics, and Git/GitHub.

## Project Overview

This project processes retail order data through an automated data pipeline.

The pipeline performs:

1. Raw data ingestion
2. Data cleaning and transformation
3. Processed data generation
4. Sales analytics
5. Automated workflow execution using Apache Airflow

## Technologies Used

- Python
- Apache Airflow
- Pandas
- Git
- GitHub
- WSL
- CSV
- SQL

## Project Structure

```text
retail-data-platform/
│
├── dags/
│   └── retail_pipeline.py
│
├── data/
│   ├── raw/
│   │   └── orders.csv
│   │
│   └── processed/
│       ├── orders_clean.csv
│       └── sales_summary.csv
│
├── analytics.py
├── transform.py
├── tes_connection.py
├── .gitignore
└── README.md

## Pipeline Flow

Raw Orders Data
       ↓
Data Cleaning
       ↓
Data Transformation
       ↓
Processed Data
       ↓
Sales Analytics
       ↓
Sales Summary



## Technologies Used

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Apache Airflow
- Git & GitHub

## How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run the data pipeline
5. Check the processed data and sales summary

## Pipeline Execution Result

The Retail Data Pipeline was successfully executed using Apache Airflow.

### Generated Outputs

- `data/processed/orders_clean.csv` - Cleaned order data
- `data/processed/sales_summary.csv` - Date-wise sales summary
- `data/processed/final_sales.csv` - Final processed sales data

### Airflow DAG

DAG: `retail_pipeline`

Status: **Success**

### Sample Sales Summary

| Order Date | Total Orders | Total Sales |
|------------|--------------|-------------|
| 2026-08-01 | 1 | 99.0 |
| 2026-08-02 | 1 | 99.0 |
| 2026-08-03 | 1 | 12.0 |
| 2026-08-04 | 1 | 19.0 |
| 2026-08-05 | 1 | 50.0 |

**Top Selling Product:** Wireless Mouse

## Author

Anish Kumar