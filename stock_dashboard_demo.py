import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Stock Dashboard Demo",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Real-Time Stock Dashboard (Demo Mode)")
st.info("🔧 Demo mode: Using simulated data. In production, this connects to Yahoo Finance API.")
st.markdown("---")

# List of stocks to track
STOCKS = ['NVDA', 'AMZN', 'TSLA', 'MA', 'ORCL']

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    auto_refresh = st.checkbox("Auto-refresh (30s)", value=False)
    
    if st.button("🔄 Refresh Now"):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("Real-time stock data powered by Yahoo Finance")
    st.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Simulated stock data
def get_mock_stock_data():
    """Generate realistic mock stock data"""
    base_data = {
        'NVDA': {
            'name': 'NVIDIA Corporation',
            'base_price': 145.50,
            'market_cap': 3.58e12,
            'pe_ratio': 68.5,
            'forward_pe': 45.2,
            'price_to_book': 48.3,
            'dividend_yield': 0.0003,
            'beta': 1.72
        },
        'AMZN': {
            'name': 'Amazon.com Inc.',
            'base_price': 178.25,
            'market_cap': 1.85e12,
            'pe_ratio': 52.3,
            'forward_pe': 38.7,
            'price_to_book': 8.9,
            'dividend_yield': 0,
            'beta': 1.15
        },
        'TSLA': {
            'name': 'Tesla Inc.',
            'base_price': 242.80,
            'market_cap': 7.72e11,
            'pe_ratio': 75.6,
            'forward_pe': 58.4,
            'price_to_book': 14.2,
            'dividend_yield': 0,
            'beta': 2.34
        },
        'MA': {
            'name': 'Mastercard Incorporated',
            'base_price': 485.60,
            'market_cap': 4.52e11,
            'pe_ratio': 35.8,
            'forward_pe': 28.9,
            'price_to_book': 58.7,
            'dividend_yield': 0.0055,
            'beta': 1.08
        },
        'ORCL': {
            'name': 'Oracle Corporation',
            'base_price': 175.35,
            'market_cap': 4.84e11,
            'pe_ratio': 36.4,
            'forward_pe': 24.5,
            'price_to_book': 45.2,
            'dividend_yield': 0.012,
            'beta': 0.92
        }
    }
    
    result = {}
    for ticker, data in base_data.items():
        # Add some random variation
        current_price = data['base_price'] * (1 + random.uniform(-0.02, 0.02))
        previous_close = data['base_price']
        change = current_price - previous_close
        change_percent = (change / previous_close) * 100
        
        # Generate intraday data
        times = pd.date_range(
            start=datetime.now().replace(hour=9, minute=30, second=0),
            end=datetime.now().replace(hour=16, minute=0, second=0),
            freq='5min'
        )
        
        # Random walk for intraday prices
        price_changes = np.random.randn(len(times)) * 0.5
        intraday_prices = previous_close + np.cumsum(price_changes)
        
        history = pd.DataFrame({
            'Close': intraday_prices
        }, index=times)
        
        result[ticker] = {
            'ticker': ticker,
            'name': data['name'],
            'current_price': current_price,
            'previous_close': previous_close,
            'change': change,
            'change_percent': change_percent,
            'market_cap': data['market_cap'],
            'pe_ratio': data['pe_ratio'],
            'forward_pe': data['forward_pe'],
            'price_to_book': data['price_to_book'],
            'dividend_yield': data['dividend_yield'],
            'beta': data['beta'],
            'fifty_two_week_high': previous_close * 1.25,
            'fifty_two_week_low': previous_close * 0.68,
            'volume': random.randint(50000000, 150000000),
            'avg_volume': random.randint(60000000, 120000000),
            'history': history
        }
    
    return result

def format_large_number(num):
    """Format large numbers into readable format"""
    if num >= 1e12:
        return f"${num/1e12:.2f}T"
    elif num >= 1e9:
        return f"${num/1e9:.2f}B"
    elif num >= 1e6:
        return f"${num/1e6:.2f}M"
    else:
        return f"${num:,.2f}"

def create_price_card(stock_data):
    """Create a price display card"""
    change_color = "green" if stock_data['change'] >= 0 else "red"
    change_symbol = "+" if stock_data['change'] >= 0 else ""
    
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 10px;'>
        <h3 style='margin: 0; color: #333;'>{stock_data['ticker']}</h3>
        <p style='margin: 5px 0; color: #666; font-size: 14px;'>{stock_data['name']}</p>
        <h2 style='margin: 10px 0; color: #000;'>${stock_data['current_price']:.2f}</h2>
        <p style='margin: 0; color: {change_color}; font-size: 16px; font-weight: bold;'>
            {change_symbol}${stock_data['change']:.2f} ({change_symbol}{stock_data['change_percent']:.2f}%)
        </p>
    </div>
    """, unsafe_allow_html=True)

def create_intraday_chart(stock_data):
    """Create an intraday price chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=stock_data['history'].index,
        y=stock_data['history']['Close'],
        mode='lines',
        name=stock_data['ticker'],
        line=dict(color='#1f77b4', width=2),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.1)'
    ))
    
    fig.update_layout(
        title=f"{stock_data['ticker']} - Intraday Price",
        xaxis_title="Time",
        yaxis_title="Price ($)",
        height=300,
        margin=dict(l=0, r=0, t=40, b=0),
        hovermode='x unified'
    )
    
    return fig

# Get mock data
stock_data_dict = get_mock_stock_data()

# Main Dashboard Section
st.header("📊 Stock Overview")

# Create columns for stock cards
cols = st.columns(len(STOCKS))

for idx, ticker in enumerate(STOCKS):
    with cols[idx]:
        create_price_card(stock_data_dict[ticker])

st.markdown("---")

# Detailed Metrics Section
st.header("📈 Detailed Metrics")

# Create tabs for each stock
tabs = st.tabs(STOCKS)

for idx, ticker in enumerate(STOCKS):
    with tabs[idx]:
        stock_data = stock_data_dict[ticker]
        
        # Display intraday chart
        fig = create_intraday_chart(stock_data)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display metrics in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Market Cap", format_large_number(stock_data['market_cap']))
            st.metric("P/E Ratio", f"{stock_data['pe_ratio']:.2f}")
            st.metric("Forward P/E", f"{stock_data['forward_pe']:.2f}")
        
        with col2:
            st.metric("Price/Book", f"{stock_data['price_to_book']:.2f}")
            st.metric("Dividend Yield", f"{stock_data['dividend_yield']*100:.2f}%")
            st.metric("Beta", f"{stock_data['beta']:.2f}")
        
        with col3:
            st.metric("52W High", f"${stock_data['fifty_two_week_high']:.2f}")
            st.metric("52W Low", f"${stock_data['fifty_two_week_low']:.2f}")
            st.metric("Volume", f"{stock_data['volume']:,}")

st.markdown("---")

# Stock Comparison Section
st.header("🔄 Stock Comparison")

col1, col2 = st.columns(2)

with col1:
    stock1 = st.selectbox("Select First Stock", STOCKS, index=0, key="stock1")

with col2:
    stock2 = st.selectbox("Select Second Stock", STOCKS, index=1, key="stock2")

if stock1 and stock2:
    st.subheader(f"Comparing {stock1} vs {stock2}")
    
    data1 = stock_data_dict[stock1]
    data2 = stock_data_dict[stock2]
    
    # Comparison metrics
    comparison_df = pd.DataFrame({
        'Metric': [
            'Current Price',
            'Market Cap',
            'P/E Ratio',
            'Forward P/E',
            'Price/Book',
            'Dividend Yield',
            'Beta',
            '52W High',
            '52W Low',
            'Day Change %'
        ],
        stock1: [
            f"${data1['current_price']:.2f}",
            format_large_number(data1['market_cap']),
            f"{data1['pe_ratio']:.2f}",
            f"{data1['forward_pe']:.2f}",
            f"{data1['price_to_book']:.2f}",
            f"{data1['dividend_yield']*100:.2f}%",
            f"{data1['beta']:.2f}",
            f"${data1['fifty_two_week_high']:.2f}",
            f"${data1['fifty_two_week_low']:.2f}",
            f"{data1['change_percent']:.2f}%"
        ],
        stock2: [
            f"${data2['current_price']:.2f}",
            format_large_number(data2['market_cap']),
            f"{data2['pe_ratio']:.2f}",
            f"{data2['forward_pe']:.2f}",
            f"{data2['price_to_book']:.2f}",
            f"{data2['dividend_yield']*100:.2f}%",
            f"{data2['beta']:.2f}",
            f"${data2['fifty_two_week_high']:.2f}",
            f"${data2['fifty_two_week_low']:.2f}",
            f"{data2['change_percent']:.2f}%"
        ]
    })
    
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # Side-by-side price charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = create_intraday_chart(data1)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = create_intraday_chart(data2)
        st.plotly_chart(fig2, use_container_width=True)
