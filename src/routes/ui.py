from flask import Blueprint, render_template,request,jsonify
import joblib
import numpy as np
from src.utils.preprocess import preprocess

ui_bp = Blueprint('ui', __name__)

model = joblib.load('models/FC110595_thathsara/diabetes_xgb_model.pkl')

@ui_bp.route('/')
def index():
    return render_template('index.html', prediction="")

@ui_bp.route('/predict', methods=['POST'])
def predict():
    data = {
        'Pregnancies': float(request.form['Pregnancies']),
        'Glucose': float(request.form['Glucose']),
        'BloodPressure': float(request.form['BloodPressure']),
        'SkinThickness': float(request.form['SkinThickness']),
        'Insulin': float(request.form['Insulin']),
        'BMI': float(request.form['BMI']),
        'DiabetesPedigreeFunction': float(request.form['DiabetesPedigreeFunction']),
        'Age': float(request.form['Age'])
    }
    print(data)
    features = preprocess(data)
    features = np.array([features])
    prediction = model.predict_proba(features)
    print(prediction)
    if prediction[0][1] > 0.5:
        result = 1
    else:
        result = 0
    prediction = "Diabetes" if result == 1 else "No Diabetes"
    return render_template('index.html', prediction=prediction)
