import pandas as pd

from sklearn.metrics import silhouette_score

import joblib

from preprocess import preprocess_data

df = pd.read_csv("data/customers.csv")

X = preprocess_data(df)

model = joblib.load("models/kmeans_model.pkl")

labels = model.predict(X)

score = silhouette_score(X, labels)

print(f"Silhouette Score: {score}")