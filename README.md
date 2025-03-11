# Bank Marketing Data Processing

This repository contains scripts and documentation for processing bank marketing campaign data. The project cleans and restructures data from a marketing campaign aimed at getting customers to take out personal loans, preparing it for import into a PostgreSQL database.

## Project Overview

The bank collected data as part of a marketing campaign and needs it cleaned and reformatted according to a specific structure and data types. The cleaned data will be used to set up a PostgreSQL database that will store this campaign's data and allow data from future campaigns to be easily imported.

## Data Structure

The original dataset `bank_marketing.csv` is processed into three separate files:

### 1. `client.csv`
Contains client demographic information:
- `client_id` (integer): Client ID
- `age` (integer): Client's age in years
- `job` (object): Client's type of job (with "." replaced by "_")
- `marital` (object): Client's marital status
- `education` (object): Client's level of education (with "." replaced by "_" and "unknown" replaced with NaN)
- `credit_default` (boolean): Whether the client's credit is in default (1 if "yes", 0 otherwise)
- `mortgage` (boolean): Whether the client has an existing mortgage (1 if "yes", 0 otherwise)

### 2. `campaign.csv`
Contains information about the marketing campaign:
- `client_id` (integer): Client ID
- `number_contacts` (integer): Number of contact attempts to the client in the current campaign
- `contact_duration` (integer): Last contact duration in seconds
- `previous_campaign_contacts` (integer): Number of contact attempts to the client in the previous campaign
- `previous_outcome` (boolean): Outcome of the previous campaign (1 if "success", 0 otherwise)
- `campaign_outcome` (boolean): Outcome of the current campaign (1 if "yes", 0 otherwise)
- `last_contact_date` (datetime): Last date the client was contacted (YYYY-MM-DD format)

### 3. `economics.csv`
Contains economic indicators:
- `client_id` (integer): Client ID
- `cons_price_idx` (float): Consumer price index (monthly indicator)
- `euribor_three_months` (float): Euro Interbank Offered Rate (euribor) three-month rate (daily indicator)

## Usage

1. Place the original `bank_marketing.csv` file in the `data/raw/` directory
2. Run the data processing script:
   ```
   python scripts/data_processing.py
   ```
3. The processed CSV files will be saved to the `data/processed/` directory

## Database Setup

The SQL script for creating the appropriate tables in PostgreSQL is provided in the `sql/create_tables.sql` file.

## Requirements

- Python 3.8+
- pandas
- numpy

To install the required packages:
```
pip install -r requirements.txt
```
