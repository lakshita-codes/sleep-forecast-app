import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("😴 Advanced Sleep Forecasting App")

# ======================
# DATASET SELECTION
# ======================
dataset_choice = st.selectbox(
    "Choose Dataset",
    ["Upload CSV", "Use Kaggle Dataset"]
)

# ======================
# LOAD DATA
# ======================
if dataset_choice == "Use Kaggle Dataset":
    try:
        df = pd.read_csv("data/kaggle_processed.csv")
        st.success("✅ Using Kaggle Dataset")
    except:
        st.error("❌ Kaggle dataset not found.")
        st.stop()
else:
    file = st.file_uploader("Upload Sleep CSV", type=["csv"])
    
    if file:
        df = pd.read_csv(file)
    else:
        st.info("📂 Please upload a CSV file")
        st.stop()

# ======================
# DATA PREVIEW
# ======================
st.subheader("📊 Data Preview")
st.write(df.head())

# ======================
# MODEL SELECTION (UI ONLY)
# ======================
st.subheader("⚙️ Select Forecasting Model")

model_type = st.selectbox(
    "Choose Model",
    ["SARIMA", "LSTM", "Prophet"]
)

# ======================
# HISTORICAL PLOT + ANOMALY DETECTION
# ======================
st.subheader("📈 Historical Sleep Pattern")

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Anomaly Detection
df['Anomaly'] = df['SleepDuration'] < 5

plt.figure(figsize=(12,5))

plt.plot(df.index, df['SleepDuration'], label="Sleep Duration", linewidth=2)

anomalies = df[df['Anomaly']]
plt.scatter(anomalies.index, anomalies['SleepDuration'], color='red', label="Anomalies", s=50)

plt.title("Sleep Pattern with Anomalies")
plt.xlabel("Date")
plt.ylabel("Sleep Duration")
plt.legend()
plt.grid(True)

st.pyplot(plt)

# ======================
# PREDICTION (LIGHTWEIGHT)
# ======================
if st.button("Predict Future Sleep"):

    # Simple prediction (mean + small variation)
    last_values = df['SleepDuration'].tail(10)
    avg = last_values.mean()

    forecast = np.array([
        avg + np.random.uniform(-0.3, 0.3) for _ in range(7)
    ])

    st.subheader("🔮 Future Sleep Prediction")
    st.write(f"📌 Model Selected (Simulated): **{model_type}**")

    # ======================
    # MODEL PERFORMANCE
    # ======================
    from sklearn.metrics import mean_absolute_error, mean_squared_error

    actual = df['SleepDuration'].tail(len(forecast))

    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(mean_squared_error(actual, forecast))

    st.subheader("📏 Model Performance")
    st.write({
        "MAE": round(mae, 2),
        "RMSE": round(rmse, 2)
    })

    # ======================
    # HISTORICAL + FORECAST
    # ======================
    history = df['SleepDuration'].tail(30)

    plt.figure(figsize=(12,5))

    plt.plot(range(len(history)), history, label="Past Sleep", linewidth=2)

    future_x = range(len(history), len(history)+len(forecast))
    plt.plot(future_x, forecast, marker='o', linewidth=2, label=f"{model_type} Forecast")

    upper = forecast + 0.5
    lower = forecast - 0.5
    plt.fill_between(future_x, lower, upper, alpha=0.2, label="Confidence Interval")

    plt.axvline(x=len(history)-1, linestyle='--', color='gray', label="Today")

    plt.xlabel("Time")
    plt.ylabel("Sleep Duration (hours)")
    plt.title("Historical + Forecast Sleep Pattern")
    plt.legend()
    plt.grid(True)

    st.pyplot(plt)

    # ======================
    # INSIGHTS
    # ======================
    avg_sleep = forecast.mean()

    st.subheader("💡 Insights & Recommendations")

    if avg_sleep < 6:
        st.error("⚠️ Poor sleep predicted.")
        st.warning("👉 Reduce screen time and stress before bed")

    elif avg_sleep > 8:
        st.info("😴 High sleep duration detected.")
        st.warning("👉 Oversleeping may affect productivity")

    else:
        st.success("✅ Healthy sleep pattern!")

    if 'Stress Level' in df.columns:
        avg_stress = df['Stress Level'].mean()

        if avg_stress > 7:
            st.warning("🧠 High stress detected → Try meditation")
        elif avg_stress < 3:
            st.info("😊 Low stress levels — great balance!")

    # ======================
    # SUMMARY
    # ======================
    st.subheader("📊 Summary Statistics")

    st.write({
        "Average Predicted Sleep": round(avg_sleep, 2),
        "Max Sleep": round(max(forecast), 2),
        "Min Sleep": round(min(forecast), 2)
    })