#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# App Title
st.title("AI-Powered Insider Trading Detection")

# Sidebar for user input
st.sidebar.header("Input Stock Ticker")

# User inputs
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Fetching stock data
def get_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

# Display the stock data
st.subheader(f"Stock Data for {ticker} from {start_date} to {end_date}")
data = get_stock_data(ticker, start_date, end_date)
st.write(data.tail())

# Feature engineering
data['Returns'] = data['Adj Close'].pct_change()
data['Moving_Avg'] = data['Adj Close'].rolling(window=20).mean()
data['Volatility'] = data['Adj Close'].rolling(window=20).std()
data = data.dropna()

# Load the pre-trained Isolation Forest model
def load_model():
    with open('isolation_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Predict anomalies
def detect_anomalies(data, model):
    features = data[['Returns', 'Moving_Avg', 'Volatility']]
    data['Anomaly'] = model.predict(features)
    return data

# Run anomaly detection
if st.button("Run Anomaly Detection"):
    result_data = detect_anomalies(data, model)
    st.subheader("Anomaly Detection Results")
    st.write(result_data.tail())

    # Plot anomalies
    st.subheader("Anomalies in Stock Price")
    plt.figure(figsize=(10, 6))
    plt.plot(result_data.index, result_data['Adj Close'], label="Stock Price")
    anomalies = result_data[result_data['Anomaly'] == -1]
    plt.scatter(anomalies.index, anomalies['Adj Close'], color='red', label="Anomalies")
    plt.legend()
    st.pyplot(plt)


# In[ ]:




