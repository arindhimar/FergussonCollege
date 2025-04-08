import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 100
age = np.random.randint(18, 60, size=n_samples)
income = np.random.randint(20000, 100000, size=n_samples)
score = np.random.randint(30, 100, size=n_samples)

# Target 1: Binary classification target (purchased)
purchased = (score + (income / 10000) + (age / 10) > 50).astype(int)

# Target 2: Regression target (spending) — add randomness
spending = (income * 0.02 + score * 5 + age * 3 + np.random.normal(0, 500, size=n_samples)).round(2)

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'income': income,
    'score': score,
    'purchased': purchased,
    'spending': spending
})

# Save to CSV
df.to_csv("sample_dataset.csv", index=False)

# Print preview
print(df.head())
