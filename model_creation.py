import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import datetime
from tensorflow.keras.optimizers import Adam

#load data
data = pd.read_csv("data/training_data.csv")
training = data['time'].values.reshape(-1, 1) 
y = data['price'].values.reshape(-1, 1)

testing_data = pd.read_csv("data/testing_data.csv")
testing = testing_data['time'].values.reshape(-1, 1)
y_test = testing_data['price'].values.reshape(-1, 1)

#create model
model = keras.Sequential(
    [
        layers.Dense(64, input_shape=(1,), activation="relu", name="input"),
        layers.Dense(32, activation="relu", name="hidden_layer1"),
        layers.Dense(16, activation="relu", name="hidden_layer2"),
        layers.Dense(1, activation="linear",name="output"),
    ]
)

#configures learning proccess
optimizer = Adam(learning_rate=0.0001)  # Default is 0.001, try 0.0001 for slower but more stable learning
model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

#model.compile(optimizer='adam', learning_rate=0.0001, loss='mse', metrics=['mae'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)              

#train the model
model.fit(training, y, validation_data=(testing, y_test), epochs=20, callbacks=[tensorboard_callback])

model.summary()

#make predictions
pred = model.predict(testing)

print("Predictions:", pred[:5])
print("Actual values:", y_test[:5])

#save 
model.save("images/learningBase/currentAiSolution.keras")
