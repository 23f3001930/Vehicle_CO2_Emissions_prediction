import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("co2.csv")

# Drop rows with missing values
df = df.dropna()

# Encode categorical features
categorical_cols = ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features and target
features = [
    'Make', 'Model', 'Vehicle Class', 'Engine Size(L)', 'Cylinders',
    'Transmission', 'Fuel Type', 'Fuel Consumption City (L/100 km)',
    'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',
    'Fuel Consumption Comb (mpg)'
]

target = 'CO2 Emissions(g/km)'

x = df[features]  # Features
y = df[target]  # Target variable

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

# Save model and encoders
with open("model.pkl", "wb") as f:
    pickle.dump({
        "model": model,
        "encoders": encoders
    }, f)

print("Model and encoders saved to model.pkl")
