import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('data/diabetes.csv')

# Misal: pisahkan fitur dan label
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Buat model dan latih
model = RandomForestClassifier()
model.fit(X, y)

# Simpan model
joblib.dump(model, 'model/random_forest_model.pkl')
