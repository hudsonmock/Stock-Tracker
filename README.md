📈 Stock Price Tracker

A comprehensive stock price tracking application built with Python and Yahoo Finance API, featuring both GUI and command-line interfaces for real-time stock market data analysis.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20|%20Windows%20|%20Linux-lightgrey.svg)

Features

GUI Version
- Modern Interface: Clean, professional design with intuitive controls
- Real-time Stock Tracking: Live price updates with color-coded changes
- Interactive Charts: Multi-period price visualization with volume data
- Portfolio Management: Add, remove, and track multiple stocks
- Detailed Stock Information: Company data, financials, and market metrics
- Auto-refresh: Continuous updates every 30 seconds
- Professional Styling: Flat design with subtle highlights

Command-Line Version
- Terminal Interface: Lightweight, fast operation
- Portfolio Dashboard: Formatted tables with live data
- Historical Analysis: Price history with statistics
- Market Overview: Major indices tracking
- Popular Stocks: Quick access to trending stocks
- Auto-refresh Mode: Background updates with keyboard controls

Quick Start

Prerequisites
- Python 3.8 or higher
- pip package manager

Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/stock-price-tracker.git
   cd stock-price-tracker
   ```

2. Set up virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

Usage

GUI Application
```bash
python stockprice.py
```

Command-Line Application
```bash
python stock_tracker_cli.py
```

Dependencies

- yfinance - Yahoo Finance API for stock data
- pandas - Data manipulation and analysis
- matplotlib - Chart generation and visualization
- tkinter - GUI framework (included with Python)
- requests - HTTP library for API calls

Supported Stock Symbols

Use standard ticker symbols from major exchanges:
- US Stocks: AAPL, GOOGL, MSFT, TSLA, AMZN, META
- Indices: ^GSPC (S&P 500), ^DJI (Dow Jones), ^IXIC (NASDAQ)
- International: Use appropriate exchange suffixes

Screenshots

GUI Interface
```
📈 Stock Price Tracker
[Stock Symbol: ____] [Add Stock] [Get Info] [Show Chart] [Remove Stock]
☑ Auto-refresh every 30 seconds

📊 Tracked Stocks          |  📋 Stock Details
Symbol | Price | Change    |  Company: Apple Inc.
AAPL   | $150.25 | +1.45%  |  Sector: Technology
GOOGL  | $2750.80 | -0.55% |  Market Cap: $2.4T
MSFT   | $410.15 | +0.82%  |  P/E Ratio: 28.5
```

CLI Interface
```bash
📈 STOCK PORTFOLIO TRACKER
================================================
Symbol     Company                   Price        Change       Volume         
------------------------------------------------
AAPL       Apple Inc.                $150.25      +$2.15       45,234,567     
GOOGL      Alphabet Inc.             $2,750.80    -$15.30      12,456,789     
MSFT       Microsoft Corporation     $410.15      +$3.30       28,901,234     
```

GUI Features

Design Elements
- **Clean Interface**: Flat design with professional color scheme
- **Responsive Layout**: Adaptable to different screen sizes
- **Color Coding**: Green/red indicators for price changes
- **Interactive Elements**: Click, hover, and keyboard shortcuts

Functionality
- **Portfolio View**: Sortable table with real-time updates
- **Stock Details**: Comprehensive company information panel
- **Chart Visualization**: Multiple time periods (1M, 3M, 6M, 1Y)
- **Error Handling**: User-friendly error messages and validation

CLI Menu Options

1. Add Stock - Track new stock symbols
2. Remove Stock - Remove from portfolio
3. View Portfolio - Display all tracked stocks
4. Stock Details - Detailed company information
5. Price History - Historical data analysis
6. Refresh All - Update all stock data
7. Popular Stocks - View trending stocks
8. Market Summary - Major indices overview
9. Auto Refresh - Continuous updates mode

Configuration

Auto-refresh Settings
- GUI: Toggle checkbox for 30-second updates
- CLI: Menu option for continuous refresh mode

Display Options
- Currency: USD (default)
- Date Format: YYYY-MM-DD
- Number Format: Comma-separated thousands

Error Handling

The application includes comprehensive error handling for:
- Invalid stock symbols
- Network connectivity issues
- API rate limiting
- Data parsing errors
- User input validation

Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Acknowledgments

- Yahoo Finance for providing free stock market data
- Python Community for excellent libraries and documentation
- Contributors who help improve this project

## 🔮 Future Enhancements

- [ ] Portfolio Value Tracking with buy/sell prices
- [ ] Price Alerts and notifications
- [ ] Technical Indicators (RSI, MACD, etc.)
- [ ] News Integration for each stock
- [ ] Export Functionality (CSV, Excel)
- [ ] Cryptocurrency Support
- [ ] Mobile App Version
- [ ] Web Interface

## 📈 Performance

- Startup Time: ~2-3 seconds
- Data Fetch: ~1-2 seconds per stock
- Memory Usage: ~50-100MB
- Network Usage: Minimal (API calls only)

---

Made by Hudson Mock
