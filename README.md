# Customer Segmentation System

A machine learning project that groups customers into clusters using K-Means clustering. The system exposes a Flask API for real-time predictions based on customer segment, state, and city.

## Project Structure

```
Customer Segmentation System/
├── app.py                 # Flask API server
├── data/
│   └── customers.csv      # Training dataset
├── models/                # Saved model artifacts (created after training)
│   ├── encoder.pkl
│   └── kmeans_model.pkl
├── src/
│   ├── preprocess.py      # Data preprocessing and encoding
│   ├── train.py           # Train and save the K-Means model
│   ├── predict.py         # CLI prediction example
│   └── evaluate.py        # Model evaluation (silhouette score)
└── requirements.txt
```

## Requirements

- Python 3.8 or later
- pip

## Setup

1. Open a terminal and navigate to the project root:

   ```powershell
   cd "c:\Users\urban\OneDrive\Desktop\Customer Segmentation System"
   ```

2. (Recommended) Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Create the `models` folder:

   ```powershell
   mkdir models
   ```

## Training the Model

Before running the API, train the model to generate the required files in `models/`:

```powershell
python src/train.py
```

This will:

- Load `data/customers.csv`
- Encode categorical features (segment, state, city)
- Train a K-Means model with 4 clusters
- Save `models/encoder.pkl` and `models/kmeans_model.pkl`

## Running the API

Start the Flask server from the project root:

```powershell
python app.py
```

The API runs at **http://127.0.0.1:5000**.

### Predict Endpoint

**POST** `/predict`

**Request body (JSON):**

```json
{
  "segment": "Consumer",
  "state": "California",
  "city": "Los Angeles"
}
```

**Response:**

```json
{
  "cluster": 0
}
```

**Example with curl:**

```powershell
curl -X POST http://127.0.0.1:5000/predict `
  -H "Content-Type: application/json" `
  -d "{\"segment\": \"Consumer\", \"state\": \"California\", \"city\": \"Los Angeles\"}"
```

## Optional Scripts

Run these from the project root after training:

| Command | Description |
|---------|-------------|
| `python src/predict.py` | Predict cluster for a sample customer |
| `python src/evaluate.py` | Print the model silhouette score |

## Quick Start

```powershell
cd "c:\Users\urban\OneDrive\Desktop\Customer Segmentation System"
pip install -r requirements.txt
mkdir models
python src/train.py
python app.py
```
