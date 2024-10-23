# Stock Anomaly Detection

This project is a **Streamlit** web application that detects anomalies in stock data based on Z-scores for daily returns and trading volume. The application uses **Yahoo Finance** (via `yfinance`) to fetch stock data, calculates Z-scores to identify anomalies, and visualizes the results using **matplotlib**.

## Features

- Fetch historical stock data using `yfinance`.
- Calculate daily returns and volume changes for the selected stock.
- Identify anomalies based on Z-scores (for daily returns and volume).
- Visualize anomalies on stock price and volume graphs.
- Interactive user interface built with Streamlit.

## Prerequisites

Before running the application, ensure you have **Python 3.7+** installed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/stock-anomaly-detection.git
    cd stock-anomaly-detection
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run App.py.py
    ```

2. In the web interface, input the stock symbol (e.g., `AAPL` for Apple), select the start and end date, and click "Analyze."

3. The application will fetch the stock data, detect anomalies in daily returns and volume, and display the results in both table and chart formats.

## Anomaly Detection Logic

- **Daily Return Z-Score**: The Z-score is calculated based on the percentage change in the stock's closing price.
- **Volume Z-Score**: The Z-score is calculated based on the percentage change in trading volume.
- Anomalies are flagged when the absolute value of the Z-score exceeds a threshold of 3 (customizable).

## Libraries Used

- [Streamlit](https://streamlit.io/): Interactive web app framework.
- [yfinance](https://pypi.org/project/yfinance/): To download stock data.
- [pandas](https://pandas.pydata.org/): For data manipulation.
- [scipy](https://www.scipy.org/): To calculate Z-scores.
- [matplotlib](https://matplotlib.org/): For plotting stock data and anomalies.

## Example

After analyzing the stock symbol `AAPL` with a specified date range, the app will display:

- A table of detected anomalies in stock price and volume.
- Two graphs: one showing the stock price with anomalies highlighted and another showing the trading volume with anomalies highlighted.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
