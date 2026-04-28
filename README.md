# 💤 Sleep Analytics & Forecasting System

## 📌 Overview

This project is an end-to-end data science solution that analyzes and forecasts sleep patterns using machine learning and interactive visualization tools. It integrates a **Power BI dashboard** for exploratory data analysis with a **Streamlit-based web application** for real-time forecasting and insights.

The system provides both **analytical understanding** and **predictive capability**, making it a complete pipeline from data exploration to deployment.

---

## 🎯 Objectives

* Analyze relationships between sleep duration, stress levels, and physical activity
* Visualize trends and correlations using interactive dashboards
* Forecast future sleep duration using time-series models
* Build and deploy an accessible web application for real-time insights

---

## 📊 Dashboard (Power BI)

The Power BI dashboard provides:

* **KPI Cards**: Average Sleep Duration, Stress Level, Physical Activity
* **Line Chart**: Sleep duration trend over time
* **Scatter Plot**: Stress vs Sleep relationship with activity impact
* **Key Insights**:

  * Higher stress levels negatively impact sleep duration
  * Increased physical activity improves sleep quality

🔗 [Power BI Dashboard](https://app.powerbi.com/groups/me/reports/c2144f43-7c53-4b60-9cb6-5c39bd32b99e?ctid=2c5bdaf4-8ff2-4bd9-bd54-7c50ab219590&pbi_source=linkShare&bookmarkGuid=a6e8a2be-0dac-45a1-ac74-2529b2213474)

---

## 🤖 Machine Learning Models

The project explores multiple forecasting approaches:

* **ARIMA / SARIMA** – Classical statistical time-series models
* **Prophet** – Trend and seasonality-based forecasting
* **LSTM (Deep Learning)** – Captures complex temporal dependencies

### ⚠️ Deployment Note

Due to cloud deployment constraints (Streamlit Cloud limitations with heavy dependencies like TensorFlow and Prophet), a **lightweight prediction approach** is used in the deployed application.

However:

* All models were **implemented and tested locally**
* Model performance was evaluated using:

  * **MAE (Mean Absolute Error)**
  * **RMSE (Root Mean Squared Error)**

This reflects a **practical trade-off between model complexity and deployability**, similar to real-world production systems.

---

## 🌐 Streamlit Web Application

An interactive web app that enables users to:

* Upload or use dataset
* Visualize sleep patterns with anomaly detection
* Generate future sleep predictions
* View performance metrics (MAE, RMSE)
* Receive personalized insights and recommendations

🔗 [Live Streamlit App](https://sleep-forecast-app-xpirbz7kdywg9atflleegz.streamlit.app/)

---

## 🛠️ Tech Stack

* **Languages**: Python
* **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib
* **ML (Local Implementation)**: TensorFlow, Prophet
* **Visualization**: Power BI
* **Deployment**: Streamlit Cloud, GitHub

---

## 📁 Project Structure

```
sleep-forecast-app/
│── data/
│── models/
│── utils/
│── streamlit_app.py
│── predict.py
│── prophet_model.py
│── lstm_model.py
│── requirements.txt
│── README.md
```

---

## 🚀 Deployment

### 🔹 Streamlit App

1. Push code to GitHub
2. Connect repository on Streamlit Cloud
3. Select `streamlit_app.py`
4. Deploy and generate public link

### 🔹 Power BI Dashboard

1. Upload `.pbix` file to Power BI Service
2. Publish to workspace
3. Generate shareable link

---

## 📈 Key Insights

* Stress and sleep exhibit a **negative correlation**
* Physical activity contributes positively to sleep quality
* Sleep patterns show **temporal variability and anomalies**
* Balanced lifestyle factors lead to more consistent sleep behavior

---

## 💡 Future Improvements

* Integrate real-time data from wearable devices
* Deploy full ML models using scalable infrastructure (e.g., Docker, FastAPI)
* Add user-specific personalized recommendations
* Implement model retraining pipeline

---

## 👩‍💻 Author

**Lakshita Singh**

---
