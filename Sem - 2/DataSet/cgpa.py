import pandas as pd
import numpy as np

# Load dataset
file_path = "Placement_Data_Full_Class.csv"
df = pd.read_csv(file_path)

# Fill missing salary values with the median salary
df['salary'].fillna(df['salary'].median(), inplace=True)

# Normalize marks to a 0-1 scale for better linearity
df['ssc_p'] = df['ssc_p'] / 100  # 10th Marks Percentage
df['hsc_p'] = df['hsc_p'] / 100  # 12th Marks Percentage
df['degree_p'] = df['degree_p'] / 100  # Degree Percentage

# Create a "Perfectly Linear" salary dataset
df_linear = df.copy()
df_linear['salary'] = (df_linear['ssc_p'] * 400000) + (df_linear['hsc_p'] * 500000) + (df_linear['degree_p'] * 600000)

# Create a "Realistic Variation" salary dataset (Adding noise)
df_realistic = df.copy()
df_realistic['salary'] = (df_realistic['ssc_p'] * 400000) + (df_realistic['hsc_p'] * 500000) + (df_realistic['degree_p'] * 600000)
df_realistic['salary'] += np.random.normal(0, 50000, size=len(df_realistic))  # Add some random noise

# Save both datasets
linear_file_path = "St_Placement_Data_Linear.csv"
realistic_file_path = "Ln_Placement_Data_Realistic.csv"

df_linear.to_csv(linear_file_path, index=False)
df_realistic.to_csv(realistic_file_path, index=False)

linear_file_path, realistic_file_path
