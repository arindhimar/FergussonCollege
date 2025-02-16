import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define possible values
diameters = np.random.randint(8, 17, size=200)  # Diameters between 8 and 16 inches
toppings = ['Margherita', 'Pepperoni', 'Veggie Delight', 'BBQ Chicken', 'Four Cheese']
bread_types = ['thick', 'thin', 'Brooklyn', 'Detroit']

# Generate random data
data = {
    'Diameter (inches)': diameters,
    'Topping': np.random.choice(toppings, size=200),
    'BreadType': np.random.choice(bread_types, size=200),
    'Extra Topping': np.random.choice([True, False], size=200),
    'Extra Cheese': np.random.choice([True, False], size=200)
}

# Create DataFrame
df = pd.DataFrame(data)

# Assign base prices
base_price = 200  # Base price in INR for the smallest size
price_per_inch = 20  # Incremental price per inch
extra_topping_price = 30  # Additional price for extra topping
extra_cheese_price = 40  # Additional price for extra cheese

# Calculate prices
df['Price (INR)'] = base_price + (df['Diameter (inches)'] - 8) * price_per_inch
df['Price (INR)'] += df['Extra Topping'] * extra_topping_price
df['Price (INR)'] += df['Extra Cheese'] * extra_cheese_price

# Save to CSV
df.to_csv('pizza_dataset2.csv', index=False)


