import numpy as np
import joblib

model = joblib.load("/tmp/knowledgeBase/currentOlsSolution.xml")
data = np.genfromtxt('/tmp/activationBase/current_activation.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

input_data = np.array([[data['time'], data['price_lag']]])
input_data_constant = np.column_stack([np.ones(1), input_data])

prediction = model.predict(input_data_constant)
real_output = data['target_price']

print("OLS Prediction happened")
print(f"Real Value: {real_output}")
print(f"Prediction: {prediction[0]}")