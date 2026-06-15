import pandas as pd
import joblib

encoder = joblib.load("models/encoder.pkl")

model = joblib.load("models/kmeans_model.pkl")

sample = pd.DataFrame({

    "segment": ["Consumer"],

    "state": ["California"],

    "city": ["Los Angeles"]

})

X = encoder.transform(sample)

cluster = model.predict(X)

print("Customer belongs to Cluster:", cluster[0])