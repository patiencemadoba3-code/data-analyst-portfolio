import pandas as pd
import numpy as np
from datetime import datetime

# --------------------------
# Step 1: Simulate messy raw hospital data
# --------------------------
data = {
    'PatientID': [101, 102, 103, 104, None, 106],
    'Name': [' Alice ', 'bob', 'CHARLIE', 'Diana', 'Eve', ' frank '],
    'DOB': ['1990-01-01', '1985/02/15', '03-12-1978', None, '1975-07-30', '1988-11-11'],
    'Diagnosis': ['flu', 'Cold', 'Flu', 'covid-19', 'Flu ', 'cold'],
    'AdmissionDate': ['2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-14', '2023-01-15'],
    'DischargeDate': ['2023-01-15', '2023-01-16', None, '2023-01-18', '2023-01-19', '2023-01-20']
}

messy_df = pd.DataFrame(data)

# Save raw data to CSV (simulate landing in cloud raw storage like AWS S3)
messy_csv_path = 'hospital_raw_data.csv'
messy_df.to_csv(messy_csv_path, index=False)

from IPython.display import display
print('✅ Sample of messy raw data:')
display(messy_df)

# --------------------------
# Step 2: Clean and prepare the data
# --------------------------
df = pd.read_csv(messy_csv_path)
print("\n✅ Raw data loaded. Starting cleaning...")

# Fix text fields: trim spaces, standardise case
df['Name'] = df['Name'].str.strip().str.capitalize()
df['Diagnosis'] = df['Diagnosis'].str.strip().str.lower()

# Fix inconsistent date formats
def clean_date(date_str):
    if pd.isna(date_str):
        return np.nan
    date_str = date_str.replace('/', '-')
    for fmt in ['%Y-%m-%d', '%d-%m-%Y']:
        try:
            return datetime.strptime(date_str, fmt).date()
        except:
            continue
    return np.nan

df['DOB'] = df['DOB'].apply(clean_date)
df['AdmissionDate'] = pd.to_datetime(df['AdmissionDate']).dt.date
df['DischargeDate'] = pd.to_datetime(df['DischargeDate']).dt.date

# Handle missing PatientID
df['PatientID'] = df['PatientID'].fillna(df['PatientID'].max() + 1).astype(int)

# Calculate useful new metric: length of stay
df['LengthOfStay_Days'] = (df['DischargeDate'] - df['AdmissionDate']).dt.days

# Save final clean dataset
clean_csv_path = 'hospital_clean_data.csv'
df.to_csv(clean_csv_path, index=False)

print("\n✅ Data cleaning complete! Sample of clean data:")
display(df)
