from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import joblib

app = Flask(__name__)

CORS(app)

encoder = joblib.load("models/encoder.pkl")

model = joblib.load("models/kmeans_model.pkl")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    df = pd.DataFrame([{

        "segment": data["segment"],

        "state": data["state"],

        "city": data["city"]

    }])

    X = encoder.transform(df)

    cluster = int(model.predict(X)[0])

    return jsonify({

        "cluster": cluster

    })


if __name__ == "__main__":
    app.run(debug=True)