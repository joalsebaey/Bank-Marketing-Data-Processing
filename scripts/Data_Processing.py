import pandas as pd
import numpy as np
import os
from datetime import datetime

def create_directory(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def process_bank_marketing_data():
    """
    Process the bank marketing data and split it into three CSV files:
    client.csv, campaign.csv, and economics.csv
    """
    # Create necessary directories
    create_directory('data/processed')
    
    # Input and output file paths
    input_file = 'data/raw/bank_marketing.csv'
    client_output = 'data/processed/client.csv'
    campaign_output = 'data/processed/campaign.csv'
    economics_output = 'data/processed/economics.csv'
    
    # Load the dataset
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} records.")
    
    # Process client data
    print("Processing client data...")
    client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()
    
    # Clean job column: replace "." with "_"
    client['job'] = client['job'].str.replace('.', '_')
    
    # Clean education column: replace "." with "_" and "unknown" with NaN
    client['education'] = client['education'].str.replace('.', '_')
    client['education'] = client['education'].replace('unknown', np.NaN)
    
    # Convert credit_default to boolean (1 if "yes", 0 otherwise)
    client['credit_default'] = client['credit_default'].apply(lambda x: 1 if x == 'yes' else 0)
    
    # Convert mortgage to boolean (1 if "yes", 0 otherwise)
    client['mortgage'] = client['mortgage'].apply(lambda x: 1 if x == 'yes' else 0)
    
    # Process campaign data
    print("Processing campaign data...")
    campaign = df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 
                  'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()
    
    # Convert previous_outcome to boolean (1 if "success", 0 otherwise)
    campaign['previous_outcome'] = campaign['previous_outcome'].apply(lambda x: 1 if x == 'success' else 0)
    
    # Convert campaign_outcome to boolean (1 if "yes", 0 otherwise)
    campaign['campaign_outcome'] = campaign['campaign_outcome'].apply(lambda x: 1 if x == 'yes' else 0)
    
    # Create last_contact_date from day, month, and year (2022)
    month_mapping = {
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
        'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
    }
    
    campaign['month_num'] = campaign['month'].str.lower().map(month_mapping)
    campaign['day_str'] = campaign['day'].astype(str).str.zfill(2)  # Ensure day is 2 digits
    campaign['last_contact_date'] = '2022-' + campaign['month_num'] + '-' + campaign['day_str']
    campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'])
    
    # Drop intermediate columns
    campaign = campaign.drop(['day', 'day_str', 'month', 'month_num'], axis=1)
    
    # Process economics data
    print("Processing economics data...")
    economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()
    
    # Save processed data
    print(f"Saving client data to {client_output}...")
    client.to_csv(client_output, index=False)
    
    print(f"Saving campaign data to {campaign_output}...")
    campaign.to_csv(campaign_output, index=False)
    
    print(f"Saving economics data to {economics_output}...")
    economics.to_csv(economics_output, index=False)
    
    print("Data processing completed successfully!")
    
    # Data verification
    print("\nData verification:")
    print(f"client.csv: {len(client)} records")
    print(f"campaign.csv: {len(campaign)} records")
    print(f"economics.csv: {len(economics)} records")

if __name__ == "__main__":
    process_bank_marketing_data()
