import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("junioralive/india-spam-sms-classification")

csv_file = None
for file in os.listdir(path):
    if file.endswith('.csv'):
        csv_file = os.path.join(path, file)
        break

if csv_file:
    print(f"Reading {csv_file}...")
    kaggle_df = pd.read_csv(csv_file, encoding='utf-8', on_bad_lines='skip')
    
    kaggle_df.rename(columns={'Label': 'v1', 'Msg': 'v2'}, inplace=True)
    
    kaggle_df = kaggle_df[['v1', 'v2']]
    
    existing_df = pd.read_csv('spam.csv', encoding='utf-8')
    
    combined_df = pd.concat([existing_df, kaggle_df], ignore_index=True)
    
    combined_df.to_csv('spam.csv', index=False, encoding='utf-8')
    print(f"Added {len(kaggle_df)} messages from Kaggle. Total rows: {len(combined_df)}")
