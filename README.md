# dashboard-stock
# 📈 Real-Time Stock Dashboard

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-FF4B4B.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen.svg)

**A beautiful, interactive dashboard for tracking real-time stock prices and financial metrics**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Customization](#-customization)

</div>

---

## 🎯 Overview

A powerful yet simple stock monitoring dashboard built with **Streamlit** and **yfinance**. Track multiple stocks simultaneously, compare performance metrics, and visualize intraday price movements—all in real-time with an intuitive, modern interface.

Perfect for investors, traders, financial analysts, or anyone interested in monitoring stock market trends.

## ✨ Features

### 📊 Real-Time Data
- **Live Stock Prices** - Continuously updated prices from Yahoo Finance
- **Automatic Refresh** - Optional 30-second auto-refresh for hands-free monitoring
- **Intraday Charts** - Interactive price movement visualization throughout the trading day

### 💼 Comprehensive Metrics
- **Valuation Metrics** - P/E Ratio, Forward P/E, Price-to-Book
- **Market Data** - Market Cap, Trading Volume, 52-Week Range
- **Risk Indicators** - Beta, Volatility Measures
- **Income Metrics** - Dividend Yield, Payout Information

### 🔄 Comparison Tools
- **Side-by-Side Analysis** - Compare any two stocks directly
- **Metric Tables** - Easy-to-read comparative data
- **Visual Charts** - Graphical comparison of price movements

### 🎨 Modern Interface
- **Clean Design** - Professional, intuitive layout
- **Responsive** - Works seamlessly on desktop, tablet, and mobile
- **Color-Coded** - Green/red indicators for quick insight
- **Tab Navigation** - Organized access to detailed stock information

## 📊 Default Tracked Stocks

| Ticker | Company | Sector |
|--------|---------|--------|
| **NVDA** | NVIDIA Corporation | Technology |
| **AMZN** | Amazon.com Inc. | Consumer Cyclical |
| **TSLA** | Tesla Inc. | Automotive |
| **MA** | Mastercard Incorporated | Financial Services |
| **ORCL** | Oracle Corporation | Technology |

*Easily customizable to track any stocks you want!*

## 🎥 Demo

### Live Dashboard
![Dashboard Overview](https://via.placeholder.com/800x400/667eea/ffffff?text=Dashboard+Overview)

### Stock Comparison
![Stock Comparison](https://via.placeholder.com/800x400/764ba2/ffffff?text=Stock+Comparison)

### Detailed Metrics
![Detailed Metrics](https://via.placeholder.com/800x400/667eea/ffffff?text=Detailed+Metrics)

*Screenshots: Add your own by running the dashboard and capturing screens*

## 🚀 Installation

### Prerequisites
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Internet connection** (for fetching stock data)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stock-dashboard.git
   cd stock-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install packages individually:
   ```bash
   pip install streamlit yfinance pandas plotly
   ```

3. **Run the dashboard**
   ```bash
   streamlit run stock_dashboard.py
   ```

4. **Open your browser**
   
   The dashboard will automatically open at `http://localhost:8501`
   
   If it doesn't open automatically, manually navigate to the URL shown in your terminal.

## 💻 Usage

### Basic Operations

**Start the Dashboard**
```bash
streamlit run stock_dashboard.py
```

**Enable Auto-Refresh**
- Toggle the "Auto-refresh (30s)" checkbox in the sidebar
- Dashboard will automatically update every 30 seconds

**Manual Refresh**
- Click the "🔄 Refresh Now" button in the sidebar
- Fetches the latest data immediately

**View Detailed Metrics**
- Click on any stock tab (NVDA, AMZN, TSLA, MA, ORCL)
- Explore comprehensive financial metrics and intraday charts

**Compare Stocks**
- Scroll to the "Stock Comparison" section
- Select two stocks from the dropdown menus
- View side-by-side metrics and charts

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Stop Dashboard | `Ctrl+C` (Windows/Linux) or `Cmd+C` (Mac) |
| Refresh Page | `R` (when focused on dashboard) |

## 🎨 Customization

### Track Different Stocks

Edit `stock_dashboard.py` and modify the `STOCKS` list (around line 16):

```python
# Default stocks
STOCKS = ['NVDA', 'AMZN', 'TSLA', 'MA', 'ORCL']

# Tech stocks
STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'META', 'NFLX']

# Market ETFs
STOCKS = ['SPY', 'QQQ', 'DIA', 'IWM', 'VTI']

# Cryptocurrencies
STOCKS = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'DOT-USD']

# Mix and match
STOCKS = ['AAPL', 'SPY', 'BTC-USD', 'TSLA', 'GOOGL']
```

### Modify Refresh Interval

Change the cache TTL in the `get_stock_data` function:

```python
@st.cache_data(ttl=60)  # 60 seconds instead of 30
def get_stock_data(ticker):
    # ...
```

### Customize Appearance

Streamlit uses a configuration file for theming. Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### Add More Metrics

Extend the dashboard by adding more data from `yfinance`:

```python
# In get_stock_data function, add:
'earnings_growth': info.get('earningsGrowth', 0),
'profit_margin': info.get('profitMargins', 0),
'debt_to_equity': info.get('debtToEquity', 0),
```

## 🛠️ Project Structure

```
stock-dashboard/
│
├── stock_dashboard.py          # Main dashboard application
├── stock_dashboard_demo.py     # Demo with simulated data (no internet)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── .gitignore                 # Git ignore rules
│
└── .streamlit/                 # (Optional) Streamlit configuration
    └── config.toml            # Theme and settings
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.31.0+ | Web framework for dashboard |
| yfinance | 0.2.36+ | Yahoo Finance API for stock data |
| pandas | 2.2.0+ | Data manipulation and analysis |
| plotly | 5.18.0+ | Interactive charting |

## 🐛 Troubleshooting

### Common Issues

**Issue: Port 8501 already in use**
```bash
# Use a different port
streamlit run stock_dashboard.py --server.port 8502
```

**Issue: Cannot connect to Yahoo Finance**
```bash
# Use the demo version with simulated data
streamlit run stock_dashboard_demo.py
```

**Issue: `streamlit: command not found`**
```bash
# Run as Python module
python -m streamlit run stock_dashboard.py

# Or use pip3/python3
pip3 install -r requirements.txt
python3 -m streamlit run stock_dashboard.py
```

**Issue: Module import errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Issue: Rate limiting from Yahoo Finance**
- The dashboard caches data for 30 seconds to minimize API calls
- If you still encounter issues, increase the cache TTL
- Use the demo version for testing without API limits

### Debug Mode

Run with verbose logging:
```bash
streamlit run stock_dashboard.py --logger.level=debug
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
- Use the [GitHub Issues](https://github.com/yourusername/stock-dashboard/issues) page
- Describe the bug and steps to reproduce
- Include your Python version and OS

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Explain your use case

### Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/stock-dashboard.git
cd stock-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -r requirements.txt
```

## 📊 Roadmap

- [ ] Historical price charts (1 week, 1 month, 1 year)
- [ ] Technical indicators (RSI, MACD, Moving Averages)
- [ ] Portfolio tracking with holdings
- [ ] Alerts and notifications for price changes
- [ ] Export data to CSV/Excel
- [ ] Dark mode theme
- [ ] Multi-currency support
- [ ] News integration for stocks
- [ ] Earnings calendar
- [ ] Watchlist management

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

## 🙏 Acknowledgments

- **[Streamlit](https://streamlit.io/)** - For the amazing framework that makes building data apps effortless
- **[yfinance](https://github.com/ranaroussi/yfinance)** - For providing free access to Yahoo Finance data
- **[Plotly](https://plotly.com/)** - For beautiful, interactive charts
- **[Pandas](https://pandas.pydata.org/)** - For powerful data manipulation tools

## 📞 Contact & Support

**Author:** Your Name  
**Email:** your.email@example.com  
**GitHub:** [@yourusername](https://github.com/yourusername)  
**Twitter:** [@yourhandle](https://twitter.com/yourhandle)

**Project Link:** [https://github.com/yourusername/stock-dashboard](https://github.com/yourusername/stock-dashboard)

### Support the Project
If you find this project helpful, please consider:
- ⭐ **Starring** the repository
- 🐛 **Reporting bugs** you encounter
- 💡 **Suggesting new features**
- 📢 **Sharing** with others who might benefit

## ⚠️ Disclaimer

**This dashboard is for informational and educational purposes only.**

- Stock data is provided by Yahoo Finance and may be delayed
- This is **NOT** financial advice
- Do not make investment decisions based solely on this tool
- Always consult with a qualified financial advisor
- Past performance does not guarantee future results
- Trading stocks involves risk of loss

The developers of this dashboard are not responsible for any financial losses incurred from using this software.

## 📚 Additional Resources

### Learn More About the Tools
- [Streamlit Documentation](https://docs.streamlit.io/)
- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Plotly Documentation](https://plotly.com/python/)

### Financial Education
- [Investopedia](https://www.investopedia.com/) - Financial terms and concepts
- [Yahoo Finance](https://finance.yahoo.com/) - Market news and data
- [SEC.gov](https://www.sec.gov/) - Official company filings

---

<div align="center">

**Made with ❤️ and Python**

If you found this helpful, please give it a ⭐!

[⬆ Back to Top](#-real-time-stock-dashboard)

</div>
