import pandas as pd
import joblib

from sklearn.cluster import KMeans

from preprocess import preprocess_data

# Load dataset
df = pd.read_csv("data/customers.csv")

# Preprocess
X = preprocess_data(df)

# Create model
model = KMeans(
    n_clusters=4,
    random_state=42
)

# Train
model.fit(X)

# Save
joblib.dump(model, "models/kmeans_model.pkl")

print("Model trained successfully.")