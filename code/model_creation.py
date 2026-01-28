import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import datetime
import numpy as np
import random

from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

#set seed for weight initialisation
SEED = 4
np.random.seed(SEED)
random.seed(SEED)
tf.random.set_seed(SEED)

#load data
data = pd.read_csv("../data/training_data.csv")
training_value_x = data[['time', 'price_lag']].values
training_value_y = data['target_price'].values.reshape(-1, 1)

testing_data = pd.read_csv("../data/testing_data.csv")
testing_value_x = testing_data[['time', 'price_lag']].values
testing_value_y = testing_data['target_price'].values.reshape(-1, 1)

#create model
model = keras.Sequential(
    [
        layers.Dense(16, kernel_initializer='normal', input_shape=(2,), activation="leaky_relu", name="input"),
        layers.Dense(8, activation="leaky_relu", name="hidden_layer1"),
        layers.Dense(1, activation="linear",name="output"),
    ]
)

#configures learning proccess
optimizer = Adam(learning_rate=0.00005)  # Default is 0.001, try 0.0001 for slower but more stable learning
model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

#creating traning and validation loss curve plot
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%d%m%Y-%H:%M:%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1, write_graph=True)

#train the model
model.fit(training_value_x, training_value_y, validation_data=(testing_value_x, testing_value_y), epochs=60, callbacks=[tensorboard_callback])
model.summary()

#make predictions
pred = model.predict(testing_value_x)
pred_training = model.predict(training_value_x)

#creating the scatter plot
plt.figure(figsize=(14,5))

pred_indices = np.arange(1, 1 + len(pred))
plt.scatter(pred_indices, testing_value_y, label="True price", s=25)
plt.plot(pred_indices, pred, label="NN prediction (Sequential)", color="red", linewidth=2)

plt.legend()
plt.title("Sequential NN Forecast vs Data Points")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()
