from prophet import Prophet
import pandas as pd

def prophet_forecast(df, steps=7):
    df = df.reset_index()
    df = df.rename(columns={'Date': 'ds', 'SleepDuration': 'y'})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=steps)
    forecast = model.predict(future)

    return forecast['yhat'].tail(steps).values