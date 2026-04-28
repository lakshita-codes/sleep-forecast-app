# 💤 Sleep Analytics & Forecasting System

## 📌 Overview

This project is an end-to-end data science solution that analyzes and predicts sleep patterns using machine learning and interactive visualization tools. It combines a Power BI dashboard for exploratory data analysis with a Streamlit-based web application for real-time forecasting.

---

## 🎯 Objectives

* Analyze the relationship between sleep duration, stress levels, and physical activity
* Visualize trends and correlations using interactive dashboards
* Forecast future sleep duration using time-series models
* Provide an accessible interface for users to explore insights and predictions

---

## 📊 Dashboard (Power BI)

The Power BI dashboard provides:

* **KPI Cards**: Average Sleep Duration, Stress Level, and Physical Activity
* **Line Chart**: Sleep duration trend over time
* **Scatter Plot**: Relationship between stress and sleep
* **Insights**:

  * Higher stress levels negatively impact sleep duration
  * Increased physical activity shows a positive influence on sleep quality

🔗 *([Power BI link here](https://app.powerbi.com/groups/me/reports/c2144f43-7c53-4b60-9cb6-5c39bd32b99e?ctid=2c5bdaf4-8ff2-4bd9-bd54-7c50ab219590&pbi_source=linkShare&bookmarkGuid=a6e8a2be-0dac-45a1-ac74-2529b2213474))*

---

## 🤖 Machine Learning Models

The project implements multiple forecasting techniques:

* **ARIMA** – Statistical time-series forecasting
* **Prophet** – Trend and seasonality modeling
* **LSTM** – Deep learning model for sequential data

---

## 🌐 Streamlit Web Application

A user-friendly web interface built with Streamlit that allows users to:

* Input data
* View predictions
* Explore insights interactively

🔗 *([Streamlit app link here](https://sleep-forecast-app-xpirbz7kdywg9atflleegz.streamlit.app/))*

---

## 🛠️ Tech Stack

* **Languages**: Python
* **Libraries**: Pandas, NumPy, Scikit-learn, TensorFlow, Prophet
* **Visualization**: Power BI, Matplotlib
* **Deployment**: Streamlit Cloud, GitHub

---

## 📁 Project Structure

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

---

## 🚀 Deployment

### 🔹 Streamlit App

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Connect repository
4. Select `streamlit_app.py`
5. Deploy

### 🔹 Power BI Dashboard

1. Upload `.pbix` file to Power BI Service
2. Publish to workspace
3. Generate shareable link

---

## 📈 Key Insights

* Stress and sleep have a negative correlation
* Physical activity positively impacts sleep quality
* Sleep patterns show variability over time

---

## 👩‍💻 Author

**Lakshita Singh**

---
