import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

def preprocess_data(df):

    # Remove columns that should not be used
    df = df.drop(columns=["id", "name"])

    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

    encoded = encoder.fit_transform(df)

    joblib.dump(encoder, "models/encoder.pkl")

    return encoded
