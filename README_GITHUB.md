# 📈 Real-Time Stock Dashboard

A beautiful and interactive Streamlit dashboard for tracking real-time stock prices and financial metrics. Monitor multiple stocks simultaneously with live data from Yahoo Finance.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **Real-Time Price Tracking** - Live stock prices with automatic 30-second refresh option
- **Comprehensive Financial Metrics**
  - Market Capitalization
  - P/E Ratio (Trailing and Forward)
  - Price-to-Book Ratio
  - Dividend Yield
  - Beta
  - 52-Week High/Low
  - Trading Volume
- **Interactive Intraday Charts** - Visual representation of price movements using Plotly
- **Stock Comparison Tool** - Side-by-side comparison of any two stocks
- **Clean, Modern UI** - Professional interface with color-coded price changes
- **Responsive Design** - Works on desktop, tablet, and mobile devices

## 📊 Tracked Stocks

By default, the dashboard tracks:
- **NVDA** - NVIDIA Corporation
- **AMZN** - Amazon.com Inc.
- **TSLA** - Tesla Inc.
- **MA** - Mastercard Incorporated
- **ORCL** - Oracle Corporation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-dashboard.git
cd stock-dashboard
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Usage

Run the dashboard:
```bash
streamlit run stock_dashboard.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

## 📦 Dependencies

- `streamlit` - Web application framework
- `yfinance` - Yahoo Finance API for stock data
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive charting library

## 🎨 Customization

### Change Tracked Stocks

Edit the `STOCKS` list in `stock_dashboard.py`:

```python
STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'META', 'NFLX']
```

You can track any valid stock ticker, including:
- Individual stocks (AAPL, GOOGL, MSFT)
- ETFs (SPY, QQQ, DIA)
- Cryptocurrencies (BTC-USD, ETH-USD)

### Modify Refresh Interval

Change the cache TTL in the `@st.cache_data` decorator:

```python
@st.cache_data(ttl=60)  # Cache for 60 seconds instead of 30
def get_stock_data(ticker):
    # ...
```

## 📸 Screenshots

### Main Dashboard
![Dashboard Overview](screenshots/dashboard.png)

### Stock Comparison
![Stock Comparison](screenshots/comparison.png)

### Detailed Metrics
![Detailed Metrics](screenshots/metrics.png)

## 🛠️ Project Structure

```
stock-dashboard/
├── stock_dashboard.py          # Main dashboard application
├── stock_dashboard_demo.py     # Demo version with simulated data
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
└── screenshots/                # Dashboard screenshots (optional)
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
streamlit run stock_dashboard.py --server.port 8502
```

### Network Issues with Yahoo Finance
Use the demo version with simulated data:
```bash
streamlit run stock_dashboard_demo.py
```

### Python Command Not Found
Try using `python3` and `pip3`:
```bash
pip3 install -r requirements.txt
python3 -m streamlit run stock_dashboard.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance API wrapper
- [Plotly](https://plotly.com/) - Interactive graphing library

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/stock-dashboard](https://github.com/yourusername/stock-dashboard)

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Note:** This dashboard uses the Yahoo Finance API through the `yfinance` library. Stock data is provided for informational purposes only and should not be considered financial advice.
