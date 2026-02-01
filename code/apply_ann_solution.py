import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("/tmp/knowledgeBase/currentAiSolution.keras")
data = np.genfromtxt('/tmp/activationBase/current_activation.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

input_data = np.array([[data['time'], data['price_lag']]])
real_output = data['target_price']

prediction = model.predict(input_data)

print("Prediction happened")
print(f"Real Value: {real_output}")
print(f"Prediction: {prediction[0][0]}")