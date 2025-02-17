import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_samples = 200  # Number of rows in the dataset

# Independent Variables
ages = np.random.randint(25, 80, num_samples)  # Age between 25 and 80
tumor_sizes = np.random.uniform(5, 50, num_samples)  # Tumor size in mm (5mm to 50mm)
clump_thickness = np.random.randint(1, 10, num_samples)  # Clump Thickness (scale 1-10)
cell_size_uniformity = np.random.randint(1, 10, num_samples)  # Cell Size Uniformity (scale 1-10)

# Generate Probability of Cancer with Strong Linear Relationship
# Removing excess noise and making it more linearly dependent on tumor size
probability_of_cancer = 0.02 * tumor_sizes + 0.005 * (clump_thickness + cell_size_uniformity) 

# Ensure values are between 0 and 1
probability_of_cancer = np.clip(probability_of_cancer, 0, 1)

# Create a DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Tumor Size': tumor_sizes,
    'Clump Thickness': clump_thickness,
    'Cell Size Uniformity': cell_size_uniformity,
    'Probability of Cancer': probability_of_cancer
})

# Save the dataset
df.to_csv("High_R2_Breast_Cancer_Probability.csv", index=False)

# Display first few rows
print(df.head())
