import pandas as pd
import numpy as np

np.random.seed(42)  # Reproducibility
n_rows = 200

data = {
    "Pizza Diameter": np.random.randint(8, 19, n_rows),  # 8-18 inches
    "Topping": np.random.choice(
        ["Pepperoni", "Mushroom", "BBQ Chicken", "Extra Cheese", "Pineapple", 
         "Sausage", "Bell Pepper", "Olive", "Ham", "Jalapeno"],
        size=n_rows,
        p=[0.25, 0.15, 0.1, 0.15, 0.05, 0.1, 0.05, 0.05, 0.05, 0.05]
    ),
    "BreadType": np.random.choice(
        ["Thick", "Thin", "Brooklyn", "Detroit"],
        size=n_rows,
        p=[0.4, 0.4, 0.1, 0.1]
    ),
    "Extra Toppings": np.random.choice([True, False], size=n_rows, p=[0.3, 0.7]),  # 30% have extra toppings
    "Extra Cheese": np.random.choice([True, False], size=n_rows, p=[0.4, 0.6]),    # 40% have extra cheese
}

df = pd.DataFrame(data)

# Calculate Price
df["Price (INR)"] = (
    df["Pizza Diameter"] * 50  # Base price: ₹50 per inch
    + np.where(df["Topping"].isin(["Pepperoni", "BBQ Chicken", "Sausage"]), 80, 40)  # Premium toppings
    + np.where(df["BreadType"].isin(["Detroit", "Brooklyn"]), 60, 0)  # Specialty bread premium
    + np.where(df["Extra Toppings"], 50, 0)  # Extra toppings cost
    + np.where(df["Extra Cheese"], 30, 0)     # Extra cheese cost
    + np.random.randint(-20, 20, n_rows)      # Random noise (±₹20)
)

# Save to CSV
df.to_csv("pizza_dataset_extended.csv", index=False)