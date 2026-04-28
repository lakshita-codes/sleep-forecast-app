import pandas as pd

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)

    # Handle naming differences
    if 'SleepDuration' not in df.columns:
        if 'Sleep Duration' in df.columns:
            df['SleepDuration'] = df['Sleep Duration']

    df = df.ffill()

    return df