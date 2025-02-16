import pandas as pd

# Load dataset
file_path = "Placement_Data_Full_Class.csv"
df = pd.read_csv(file_path)

# Select only relevant columns
df = df[['ssc_p', 'hsc_p', 'degree_p']]  # Keeping only academic scores

# Reduce dataset size (Optional: You can change 100 to another number)
df = df.sample(n=10, random_state=42)  # Select 100 rows for a smaller dataset

# Generate "Perfectly Linear" salary values using exact integer multipliers
df['salary'] = (df['ssc_p'] * 40000) + (df['hsc_p'] * 50000) + (df['degree_p'] * 60000)

# Save the dataset
df.to_csv("Perfect_Linear_Salary.csv", index=False)

print("✅ Perfectly Linear Dataset Created!")
