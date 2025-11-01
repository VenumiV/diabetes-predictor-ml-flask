from flask import Blueprint, render_template, request, jsonify
import joblib
import numpy as np
from src.utils.preprocess import preprocess  # your preprocessing function

ui_bp = Blueprint('ui', __name__)

# Load the trained model once
model = joblib.load('models/FC212029_Venumi/random_forest_model.pkl')

@ui_bp.route('/')
def index():
    return render_template('index.html')

@ui_bp.route('/predict', methods=['GET'])
def show_predict_page():
    return render_template('predict.html')

@ui_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        # preprocess -> must return python-list or numpy array
        features = preprocess(data)
        features = np.array([features])

        # model prediction
        proba = model.predict_proba(features)[0][1]     # this is a numpy float
        proba = float(proba)                            # 👉 convert to python float

        result = 1 if proba > 0.5 else 0
        prediction_str = "Positive" if result == 1 else "Negative"

        # make probability in %
        prob_percent = round(proba * 100, 2)
        prob_percent = float(prob_percent)              # 👉 ensure JSON serializable

        response = {
            "prediction": prediction_str,
            "probability": prob_percent
        }
        print("Response:", response)
        return jsonify(response)

    except Exception as e:
        print("Error in /predict:", e)
        return jsonify({"error": str(e)}), 500
