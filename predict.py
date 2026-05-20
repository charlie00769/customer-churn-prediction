import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Example input (replace with real values)
sample = np.array([[128, 415, 25, 200, 100, 50, 180, 90, 40, 200, 100, 50, 10, 3, 2.7, 1, 0, 1]])

# Scale input
sample_scaled = scaler.transform(sample)

# Predict
prediction = model.predict(sample_scaled)

print("Churn Prediction:", "Yes" if prediction[0] == 1 else "No")