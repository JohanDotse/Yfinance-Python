# Installation
pip install yfinance

import yfinance as yf

# Tickers
tickers = {
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Natural Gas": "NG=F",
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD"
}

# Fetch and display prices
for name, ticker in tickers.items():
    asset = yf.Ticker(ticker)
    current_price = asset.info['regularMarketPrice']
    print(f"Current {name} Price: ${current_price:.2f}")
