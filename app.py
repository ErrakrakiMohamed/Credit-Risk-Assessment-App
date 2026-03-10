import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
try:
    model = joblib.load("credit_risk_model.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded. Please check server logs."}), 500

    try:
        data = request.json

        # Create a DataFrame from inputs
        input_data = pd.DataFrame(
            {
                "fico_range_low": [float(data.get("fico_range_low", 700))],
                "annual_inc": [float(data.get("annual_inc", 48000))],
                "dti": [float(data.get("dti", 20))],
                "loan_amnt": [float(data.get("loan_amnt", 9000))],
                "revol_bal": [float(data.get("revol_bal", 5000))],
            }
        )

        # Probability of approval (class 1)
        prob = model.predict_proba(input_data)[0][1]

        return jsonify({"probability": float(prob)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Runs the application on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
