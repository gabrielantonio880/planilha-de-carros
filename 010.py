import pandas as pd
import glob
import os

files = glob.glob('*')
print("Files:", files)

# Find the csv file
csv_file = [f for f in files if f.endswith('.csv')][0] if any(f.endswith('.csv') for f in files) else None
print("CSV File:", csv_file)

if csv_file:
    df = pd.read_csv(csv_file)
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nHead:")
    print(df.head())
    print("\nInfo:")
    print(df.info())
    print("\nDescribe:")
    print(df.describe(include='all'))