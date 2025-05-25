import flask
from flask import session, redirect, url_for
import numpy as np
import joblib
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

# Inisialisasi aplikasi Flask
app = flask.Flask(__name__, template_folder='templates')

# Menambahkan Secret Key untuk Session
app.secret_key = 'ini-adalah-kunci-rahasia-yang-sangat-aman-12345'

# Muat model dan scaler
try:
    model = joblib.load('model_prediksi.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model dan scaler berhasil dimuat")
except Exception as e:
    print(f"Error saat memuat model atau scaler: {e}")
    model, scaler = None, None

# Rute untuk menampilkan halaman utama (GET)
@app.route('/')
def main():
    result_text = session.pop('result', None) 
    return flask.render_template('index.html', result=result_text)

# === PERUBAHAN UTAMA DI SINI ===
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Jika ada yang mencoba akses URL ini langsung (metode GET),
    # alihkan saja ke halaman utama.
    if flask.request.method == 'GET':
        return redirect(url_for('main'))

    # Jika metodenya POST (dikirim dari form), lanjutkan proses prediksi
    if flask.request.method == 'POST':
        if model and scaler:
            # Ambil input dari pengguna lewat form
            pregnancies = float(flask.request.form['pregnancies'])
            glucose = float(flask.request.form['glucose'])
            blood_pressure = float(flask.request.form['blood_pressure'])
            skin_thickness = float(flask.request.form['skin_thickness'])
            insulin = float(flask.request.form['insulin'])
            bmi = float(flask.request.form['bmi'])
            dpf = float(flask.request.form['dpf'])
            age = float(flask.request.form['age'])

            # Lakukan Feature Engineering
            bmi_x_age = bmi * age
            glucose_x_bp = glucose * blood_pressure
            preg_x_age = pregnancies * age

            # Gabungkan semua fitur
            input_variables = pd.DataFrame([[
                pregnancies, glucose, blood_pressure, skin_thickness, 
                insulin, bmi, dpf, age, 
                bmi_x_age, glucose_x_bp, preg_x_age
            ]])

            # Lakukan scaling dan prediksi
            scaled_input = scaler.transform(input_variables)
            prediction = model.predict(scaled_input)[0]
            
            result_text = "Berisiko Tinggi Terkena Diabetes Gestasional" if prediction == 1 else "Berisiko Rendah Terkena Diabetes Gestasional"

            # Simpan hasil ke session
            session['result'] = result_text
        
        else:
            session['result'] = "Error: Model tidak berhasil dimuat."

        # Redirect kembali ke halaman utama
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)