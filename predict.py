import joblib
import numpy as np

from utils.preprocess import preprocess_data
from lstm_model import train_lstm
from prophet_model import prophet_forecast


def predict_sleep(df, model_type="SARIMA", steps=7):
    df = preprocess_data(df)

    # ======================
    # ARIMA / SARIMA
    # ======================
    if model_type == "SARIMA":
        model = joblib.load("models/arima_model.pkl")
        forecast = model.forecast(steps=steps)
        return forecast.values

    # ======================
    # LSTM
    # ======================
    elif model_type == "LSTM":
        model, scaler = train_lstm(df)

        data = df['SleepDuration'].values.reshape(-1,1)
        scaled_data = scaler.transform(data)

        last_seq = scaled_data[-10:]
        preds = []

        for _ in range(steps):
            pred = model.predict(last_seq.reshape(1,10,1), verbose=0)
            preds.append(pred[0][0])
            last_seq = np.append(last_seq[1:], pred)

        preds = scaler.inverse_transform(np.array(preds).reshape(-1,1))
        return preds.flatten()

    # ======================
    # PROPHET
    # ======================
    elif model_type == "Prophet":
        return prophet_forecast(df, steps)