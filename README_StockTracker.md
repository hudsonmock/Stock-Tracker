# 📈 Stock Price Tracker

A comprehensive stock price tracking application using Yahoo Finance API with both GUI and command-line interfaces.

## Features

### GUI Version (`stockprice.py`)
- **Real-time stock data** fetching from Yahoo Finance
- **Beautiful graphical interface** with dark theme
- **Multiple stock tracking** in a portfolio view
- **Interactive price charts** with multiple time periods
- **Detailed stock information** including financials
- **Auto-refresh functionality** (every 30 seconds)
- **Professional layout** with treeview and scrollable details

### Command-Line Version (`stock_tracker_cli.py`)
- **Terminal-based interface** for lightweight usage
- **Portfolio management** with add/remove functionality
- **Real-time price updates** and portfolio summary
- **Historical price data** with multiple time periods
- **Market summary** with major indices (S&P 500, Dow Jones, NASDAQ)
- **Popular stocks overview**
- **Auto-refresh mode** with keyboard interrupt support

## Installation

1. **Clone or download the files**
2. **Set up virtual environment:**
   ```bash
   cd "Python Projects"
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Version
```bash
source .venv/bin/activate
python stockprice.py
```

**Features:**
- Enter stock symbols (e.g., AAPL, GOOGL, MSFT)
- Click "Add Stock" to track in portfolio
- Click "Get Info" for detailed company information
- Click "Show Chart" for interactive price charts
- Double-click stocks in the list for quick details
- Enable auto-refresh for real-time updates

### Command-Line Version
```bash
source .venv/bin/activate
python stock_tracker_cli.py
```

**Menu Options:**
1. **Add Stock** - Track a new stock symbol
2. **Remove Stock** - Remove from tracking list
3. **View Portfolio** - See all tracked stocks with prices
4. **Stock Details** - Detailed information for specific stock
5. **Price History** - Historical data with statistics
6. **Refresh All** - Update all tracked stocks
7. **Popular Stocks** - View trending stocks
8. **Market Summary** - Major market indices
9. **Auto Refresh** - Continuous 30-second updates
0. **Exit** - Quit application

## Stock Symbols

Use standard ticker symbols:
- **Apple:** AAPL
- **Google:** GOOGL
- **Microsoft:** MSFT
- **Tesla:** TSLA
- **Amazon:** AMZN
- **Meta:** META
- **Netflix:** NFLX
- **NVIDIA:** NVDA

## Sample Usage

### Adding Stocks
```
Enter stock symbol: AAPL
✅ AAPL added successfully!
```

### Portfolio View
```
📈 STOCK PORTFOLIO TRACKER
================================================
Symbol     Company                   Price        Change       Change %     Volume         
------------------------------------------------
AAPL       Apple Inc.                $150.25      +$2.15       +1.45%       45,234,567     
GOOGL      Alphabet Inc.             $2,750.80    -$15.30      -0.55%       12,456,789     
```

### Detailed Information
```
📊 DETAILED INFORMATION FOR AAPL
============================================
Company Name: Apple Inc.

💰 PRICE INFORMATION
------------------------------
Current Price: $150.25
Day High: $152.10
Day Low: $148.90
52 Week High: $182.94
52 Week Low: $124.17
Change: +$2.15 (+1.45%)

📈 MARKET INFORMATION
------------------------------
Market Cap: $2,456,789,123,456
Volume: 45,234,567
P/E Ratio: 28.5
```

## Dependencies

- **yfinance**: Yahoo Finance API for stock data
- **pandas**: Data manipulation and analysis
- **matplotlib**: Plotting and visualization
- **tkinter**: GUI framework (built-in with Python)
- **requests**: HTTP library for API calls

## Error Handling

The application includes robust error handling:
- Invalid stock symbols
- Network connectivity issues
- API rate limiting
- Data parsing errors
- User input validation

## Technical Details

### Data Sources
- **Yahoo Finance API** via `yfinance` library
- Real-time and historical stock data
- Company financial information
- Market indices and statistics

### GUI Implementation
- **Tkinter** for cross-platform GUI
- **Matplotlib** integration for charts
- Threaded auto-refresh to prevent UI blocking
- Professional styling with consistent color scheme

### CLI Implementation
- Cross-platform terminal clearing
- Formatted tables and statistics
- Keyboard interrupt handling
- Color indicators for price changes

## Troubleshooting

### Import Errors
If you see import errors, ensure the virtual environment is activated:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Connection Errors
- Check internet connectivity
- Yahoo Finance may temporarily block requests
- Try again after a few minutes

### GUI Issues
- Ensure you have tkinter installed (usually comes with Python)
- On Linux: `sudo apt-get install python3-tk`
- On macOS: Usually included with Python

## Future Enhancements

Potential improvements:
- **Portfolio value tracking** with buy/sell prices
- **Alerts and notifications** for price targets
- **Export functionality** for data and charts
- **More technical indicators** and analysis
- **Cryptocurrency support**
- **News integration** for each stock
- **Watchlists and favorites**

## Contributing

Feel free to fork and improve this project! Some areas for contribution:
- Additional chart types and indicators
- Enhanced UI/UX design
- More data sources and APIs
- Mobile app version
- Web interface

## License

This project is open source and available under the MIT License.

---

**Happy Trading! 📈💰**
