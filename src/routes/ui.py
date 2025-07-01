from flask import Blueprint, render_template,request,jsonify
import joblib
import numpy as np
from src.utils.preprocess import preprocess

ui_bp = Blueprint('ui', __name__)

model = joblib.load('../../models/FC110595_thathsara/diabetes_xgb_model.pkl')

@ui_bp.route('/')
def index():
    return render_template('../templates/index.html', prediction="")

@ui_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = preprocess(data)
    prediction = model.predict(np.array(features))
    result = int(prediction[0])
    prediction = "Diabetes" if result == 1 else "No Diabetes"
    return render_template('../templates/index.html', prediction=prediction)
