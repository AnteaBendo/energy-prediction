import requests
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#Download markdown file
url = "https://raw.githubusercontent.com/AnteaBendo/energy-prediction/refs/heads/main/data/data.md"
dataset_markdown = requests.get(url).json()

time = np.array(dataset_markdown['unix_seconds'])
price = np.array(dataset_markdown['price'])

# Z-score: (x - mean) / standard_deviation
time = (time - time.mean()) / time.std()
price = (price - price.mean()) / price.std()

df = pd.DataFrame({
    "time": time.flatten(),
    "price": price.flatten()
})

#Save
df.to_csv("data/joint_data_collection.csv", index=False)

#Split data
x = df["time"].values
y = df["price"].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

df_train = pd.DataFrame({
    "time": x_train.flatten(),
    "price": y_train.flatten()
})

df_test = pd.DataFrame({
    "time": x_test.flatten(),
    "price": y_test.flatten()
})

#Save
df_train.to_csv("data/training_data.csv", index=False)
df_test.to_csv("data/testing_data.csv", index=False)

#Activation data
one_row = df.sample(1) 
one_row.to_csv("data/activation_data.csv", index=False)