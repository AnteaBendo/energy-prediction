import numpy as np
import joblib

model = joblib.load("currentOlsSolution.xml")

data = np.genfromtxt('currentActivation.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

input_data = np.array([[data['time'], data['target_price']]])
real_output = data['target_price']

# 4. Run prediction
prediction = model.predict(input_data)

print("OLS Prediction happened")
print(f"Real Value: {real_output}")
print(f"Prediction: {prediction[0]}")