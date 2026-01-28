import requests
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler

#scrape the data from git
url = "https://raw.githubusercontent.com/AnteaBendo/energy-prediction/refs/heads/main/data/data.md"
dataset_markdown = requests.get(url).json()

time = np.array(dataset_markdown['unix_seconds'])
price = np.array(dataset_markdown['price'])

df = pd.DataFrame({
    "time": time.flatten(),
    "price": price.flatten()
})

#calculate the absolute Z-score for the 'price' column
z_scores = stats.zscore(df['price'])
abs_z_scores = np.abs(z_scores)
threshold = 3

#create a mask to keep only rows within the threshold
filtered_entries = abs_z_scores < threshold
df_clean = df[filtered_entries]

df_clean['price_lag'] = df_clean['price'].shift(24)
df_clean.dropna(inplace=True)

# split the dataset into training and testing
split_idx = int(len(df_clean) * 0.8)
train_df = df_clean.iloc[:split_idx]
test_df = df_clean.iloc[split_idx:]

# create scalers
scaler_x = StandardScaler()
scaler_y = StandardScaler()

x_train = scaler_x.fit_transform(train_df[['time', 'price_lag']])
y_train = scaler_y.fit_transform(train_df[['price']])

x_test = scaler_x.transform(test_df[['time', 'price_lag']])
y_test = scaler_y.transform(test_df[['price']])

#rebuild the df using the multi-column x arrays
df_train_scaled = pd.DataFrame(x_train, columns=['time', 'price_lag'])
df_train_scaled['target_price'] = y_train

df_test_scaled = pd.DataFrame(x_test, columns=['time', 'price_lag'])
df_test_scaled['target_price'] = y_test

#save created datasets
df_train_scaled.to_csv("training_data.csv", index=False)
df_test_scaled.to_csv("testing_data.csv", index=False)

df_combined_scaled = pd.concat([df_train_scaled, df_test_scaled], axis=0)
df_combined_scaled = df_combined_scaled.reset_index(drop=True)
df_combined_scaled.to_csv("joint_data_collection.csv", index=False)

#activation data
#we take the last row of the test set so the model has the "most recent" lag
one_row = df_test_scaled.tail(1)
one_row.to_csv("activation_data.csv", index=False)

print(f"Original: {len(df)} | Cleaned: {len(df_clean)}")