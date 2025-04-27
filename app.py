from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model/random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    glucose = float(request.form['glucose'])
    insulin = float(request.form['insulin'])

    # Default values for other features
    pregnancies = 2
    blood_pressure = 72
    skin_thickness = 25
    bmi = 28.5
    dpf = 0.5

    features = np.array([[pregnancies, glucose, blood_pressure,
                          skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(features)[0]
    hasil = "Berisiko Diabetes" if prediction == 1 else "Tidak Berisiko Diabetes"

    return render_template('predict.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
