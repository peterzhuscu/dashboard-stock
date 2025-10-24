import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Real-Time Stock Dashboard")
st.markdown("---")

# List of stocks to track
STOCKS = ['NVDA', 'AMZN', 'TSLA', 'MA', 'ORCL']

# Sidebar for refresh and settings
with st.sidebar:
    st.header("⚙️ Settings")
    auto_refresh = st.checkbox("Auto-refresh (30s)", value=False)
    if auto_refresh:
        st.rerun()
    
    if st.button("🔄 Refresh Now"):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("Real-time stock data powered by Yahoo Finance")
    st.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@st.cache_data(ttl=30)
def get_stock_data(ticker):
    """Fetch stock data and financial metrics"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1d", interval="1m")
        
        # Extract key metrics
        data = {
            'ticker': ticker,
            'name': info.get('longName', ticker),
            'current_price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
            'previous_close': info.get('previousClose', 0),
            'market_cap': info.get('marketCap', 0),
            'pe_ratio': info.get('trailingPE', 0),
            'forward_pe': info.get('forwardPE', 0),
            'price_to_book': info.get('priceToBook', 0),
            'dividend_yield': info.get('dividendYield', 0),
            'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 0),
            'fifty_two_week_low': info.get('fiftyTwoWeekLow', 0),
            'volume': info.get('volume', 0),
            'avg_volume': info.get('averageVolume', 0),
            'beta': info.get('beta', 0),
            'history': hist
        }
        
        # Calculate price change
        if data['previous_close'] and data['current_price']:
            data['change'] = data['current_price'] - data['previous_close']
            data['change_percent'] = (data['change'] / data['previous_close']) * 100
        else:
            data['change'] = 0
            data['change_percent'] = 0
            
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
        return None

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
    if not stock_data:
        return
    
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
    if stock_data and not stock_data['history'].empty:
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=stock_data['history'].index,
            y=stock_data['history']['Close'],
            mode='lines',
            name=stock_data['ticker'],
            line=dict(color='#1f77b4', width=2)
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
    return None

# Main Dashboard Section
st.header("📊 Stock Overview")

# Create columns for stock cards
cols = st.columns(len(STOCKS))

# Fetch and display data for all stocks
stock_data_dict = {}
for idx, ticker in enumerate(STOCKS):
    with cols[idx]:
        stock_data = get_stock_data(ticker)
        stock_data_dict[ticker] = stock_data
        create_price_card(stock_data)

st.markdown("---")

# Detailed Metrics Section
st.header("📈 Detailed Metrics")

# Create tabs for each stock
tabs = st.tabs(STOCKS)

for idx, ticker in enumerate(STOCKS):
    with tabs[idx]:
        stock_data = stock_data_dict[ticker]
        if stock_data:
            # Display intraday chart
            fig = create_intraday_chart(stock_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            
            # Display metrics in columns
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Market Cap", format_large_number(stock_data['market_cap']))
                st.metric("P/E Ratio", f"{stock_data['pe_ratio']:.2f}" if stock_data['pe_ratio'] else "N/A")
                st.metric("Forward P/E", f"{stock_data['forward_pe']:.2f}" if stock_data['forward_pe'] else "N/A")
            
            with col2:
                st.metric("Price/Book", f"{stock_data['price_to_book']:.2f}" if stock_data['price_to_book'] else "N/A")
                st.metric("Dividend Yield", f"{stock_data['dividend_yield']*100:.2f}%" if stock_data['dividend_yield'] else "N/A")
                st.metric("Beta", f"{stock_data['beta']:.2f}" if stock_data['beta'] else "N/A")
            
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
    
    if data1 and data2:
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
                f"{data1['pe_ratio']:.2f}" if data1['pe_ratio'] else "N/A",
                f"{data1['forward_pe']:.2f}" if data1['forward_pe'] else "N/A",
                f"{data1['price_to_book']:.2f}" if data1['price_to_book'] else "N/A",
                f"{data1['dividend_yield']*100:.2f}%" if data1['dividend_yield'] else "N/A",
                f"{data1['beta']:.2f}" if data1['beta'] else "N/A",
                f"${data1['fifty_two_week_high']:.2f}",
                f"${data1['fifty_two_week_low']:.2f}",
                f"{data1['change_percent']:.2f}%"
            ],
            stock2: [
                f"${data2['current_price']:.2f}",
                format_large_number(data2['market_cap']),
                f"{data2['pe_ratio']:.2f}" if data2['pe_ratio'] else "N/A",
                f"{data2['forward_pe']:.2f}" if data2['forward_pe'] else "N/A",
                f"{data2['price_to_book']:.2f}" if data2['price_to_book'] else "N/A",
                f"{data2['dividend_yield']*100:.2f}%" if data2['dividend_yield'] else "N/A",
                f"{data2['beta']:.2f}" if data2['beta'] else "N/A",
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
            if fig1:
                st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = create_intraday_chart(data2)
            if fig2:
                st.plotly_chart(fig2, use_container_width=True)

# Auto-refresh logic
if auto_refresh:
    import time
    time.sleep(30)
    st.rerun()
