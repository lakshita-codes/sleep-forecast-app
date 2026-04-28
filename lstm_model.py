import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_lstm(df):
    data = df['SleepDuration'].values.reshape(-1,1)

    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    X, y = [], []

    for i in range(10, len(data_scaled)):
        X.append(data_scaled[i-10:i])
        y.append(data_scaled[i])

    X, y = np.array(X), np.array(y)

    model = Sequential()
    model.add(LSTM(50, return_sequences=False, input_shape=(X.shape[1],1)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, batch_size=16, verbose=0)

    return model, scaler