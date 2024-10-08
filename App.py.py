import streamlit as st
import yfinance as yf
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import io

# Define function to fetch and process data
def fetch_and_process_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    data['Daily Return'] = data['Close'].pct_change()
    data['Volume Change'] = data['Volume'].pct_change()
    data = data.dropna()

    # Calculate Z-scores
    data['Return Z-Score'] = stats.zscore(data['Daily Return'])
    data['Volume Z-Score'] = stats.zscore(data['Volume Change'])

    # Define thresholds for anomaly detection
    return_threshold = 3
    volume_threshold = 3

    # Flag anomalies
    data['Return Anomaly'] = data['Return Z-Score'].abs() > return_threshold
    data['Volume Anomaly'] = data['Volume Z-Score'].abs() > volume_threshold

    return data

# Define function to plot data
def plot_data(data, anomalies, stock_symbol):
    # Plot closing price and highlight anomalies
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(data.index, data['Close'], label='Close Price', color='blue')
    ax.scatter(anomalies.index, anomalies['Close'], color='red', label='Anomalies')
    ax.set_title(f'{stock_symbol} - Closing Price with Detected Anomalies')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)

    # Plot volume and highlight anomalies
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(data.index, data['Volume'], label='Volume', color='blue')
    ax.scatter(anomalies.index, anomalies['Volume'], color='red', label='Anomalies')
    ax.set_title(f'{stock_symbol} - Trading Volume with Detected Anomalies')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    ax.legend()
    st.pyplot(fig)

# Streamlit UI
st.title('Stock Anomaly Detection')
stock_symbol = st.text_input('Stock Symbol', 'AAPL')
start_date = st.date_input('Start Date', pd.to_datetime('2023-01-01'))
end_date = st.date_input('End Date', pd.to_datetime('2023-12-31'))

if st.button('Analyze'):
    with st.spinner('Fetching and processing data...'):
        data = fetch_and_process_data(stock_symbol, start_date, end_date)
        anomalies = data[(data['Return Anomaly']) | (data['Volume Anomaly'])]

        st.write(f"Anomalies detected: {len(anomalies)}")
        st.dataframe(anomalies)

        plot_data(data, anomalies, stock_symbol)
import sys
st.write(f"Python version: {sys.version}")

