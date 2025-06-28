#!/usr/bin/env python3
"""
Simple Stock Price Tracker - Command Line Version
================================================

A simple command-line interface for tracking stock prices using Yahoo Finance API.
This version doesn't require GUI libraries and can run in any terminal.

Author: Assistant
Date: June 2025
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
import os
import sys

class SimpleStockTracker:
    def __init__(self):
        self.tracked_stocks = {}
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_stock_data(self, symbol):
        """Get stock data for a given symbol"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            hist = ticker.history(period="1d")
            
            if hist.empty:
                return None
            
            current_price = hist['Close'].iloc[-1]
            prev_close = info.get('previousClose', current_price)
            change = current_price - prev_close
            change_percent = (change / prev_close) * 100
            volume = hist['Volume'].iloc[-1] if 'Volume' in hist.columns else 0
            
            return {
                'symbol': symbol,
                'price': current_price,
                'change': change,
                'change_percent': change_percent,
                'volume': volume,
                'company_name': info.get('longName', 'N/A'),
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('trailingPE', 'N/A'),
                'day_high': info.get('dayHigh', 'N/A'),
                'day_low': info.get('dayLow', 'N/A'),
                'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
                'fifty_two_week_low': info.get('fiftyTwoWeekLow', 'N/A')
            }
        except Exception as e:
            print(f"❌ Error fetching data for {symbol}: {e}")
            return None
    
    def add_stock(self, symbol):
        """Add a stock to tracking list"""
        symbol = symbol.upper()
        print(f"📊 Fetching data for {symbol}...")
        
        stock_data = self.get_stock_data(symbol)
        if stock_data:
            self.tracked_stocks[symbol] = stock_data
            print(f"✅ {symbol} added successfully!")
        else:
            print(f"❌ Failed to add {symbol}")
    
    def remove_stock(self, symbol):
        """Remove a stock from tracking list"""
        symbol = symbol.upper()
        if symbol in self.tracked_stocks:
            del self.tracked_stocks[symbol]
            print(f"✅ {symbol} removed from tracking list")
        else:
            print(f"❌ {symbol} not found in tracking list")
    
    def display_portfolio(self):
        """Display all tracked stocks in a nice format"""
        if not self.tracked_stocks:
            print("📭 No stocks are currently being tracked.")
            return
        
        self.clear_screen()
        print("=" * 100)
        print("📈 STOCK PORTFOLIO TRACKER")
        print("=" * 100)
        print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Header
        print(f"{'Symbol':<10} {'Company':<25} {'Price':<12} {'Change':<12} {'Change %':<12} {'Volume':<15}")
        print("-" * 100)
        
        # Stock data
        for symbol, data in self.tracked_stocks.items():
            change_str = f"${data['change']:+.2f}"
            change_percent_str = f"{data['change_percent']:+.2f}%"
            
            # Add color indicators
            if data['change'] >= 0:
                change_indicator = "🟢"
            else:
                change_indicator = "🔴"
            
            company_name = data['company_name'][:22] + "..." if len(data['company_name']) > 25 else data['company_name']
            
            print(f"{symbol:<10} {company_name:<25} ${data['price']:<11.2f} {change_str:<12} {change_percent_str:<12} {data['volume']:<15,}")
        
        print("-" * 100)
        
        # Summary
        total_value = sum(data['price'] for data in self.tracked_stocks.values())
        avg_change = sum(data['change_percent'] for data in self.tracked_stocks.values()) / len(self.tracked_stocks)
        
        print(f"📊 Portfolio Summary:")
        print(f"   Total Stocks: {len(self.tracked_stocks)}")
        print(f"   Average Price: ${total_value / len(self.tracked_stocks):.2f}")
        print(f"   Average Change: {avg_change:+.2f}%")
        print()
    
    def display_detailed_info(self, symbol):
        """Display detailed information for a specific stock"""
        symbol = symbol.upper()
        if symbol not in self.tracked_stocks:
            print(f"❌ {symbol} not found in tracking list")
            return
        
        data = self.tracked_stocks[symbol]
        
        print("=" * 60)
        print(f"📊 DETAILED INFORMATION FOR {symbol}")
        print("=" * 60)
        print(f"Company Name: {data['company_name']}")
        print()
        
        print("💰 PRICE INFORMATION")
        print("-" * 30)
        print(f"Current Price: ${data['price']:.2f}")
        print(f"Day High: ${data['day_high']}")
        print(f"Day Low: ${data['day_low']}")
        print(f"52 Week High: ${data['fifty_two_week_high']}")
        print(f"52 Week Low: ${data['fifty_two_week_low']}")
        print(f"Change: ${data['change']:+.2f} ({data['change_percent']:+.2f}%)")
        print()
        
        print("📈 MARKET INFORMATION")
        print("-" * 30)
        print(f"Market Cap: ${data['market_cap']:,}" if data['market_cap'] != 'N/A' else f"Market Cap: {data['market_cap']}")
        print(f"Volume: {data['volume']:,}")
        print(f"P/E Ratio: {data['pe_ratio']}")
        print()
    
    def refresh_all(self):
        """Refresh data for all tracked stocks"""
        if not self.tracked_stocks:
            print("📭 No stocks to refresh")
            return
        
        print("🔄 Refreshing all stocks...")
        symbols_to_update = list(self.tracked_stocks.keys())
        
        for symbol in symbols_to_update:
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                self.tracked_stocks[symbol] = stock_data
                print(f"✅ {symbol} updated")
            else:
                print(f"❌ Failed to update {symbol}")
        
        print("✅ Refresh completed!")
    
    def get_price_history(self, symbol, period="1mo"):
        """Get and display price history for a stock"""
        symbol = symbol.upper()
        print(f"📊 Fetching {period} price history for {symbol}...")
        
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            
            if hist.empty:
                print(f"❌ No historical data found for {symbol}")
                return
            
            print(f"\n📈 {symbol} - {period.upper()} PRICE HISTORY")
            print("=" * 60)
            print(f"{'Date':<12} {'Open':<10} {'High':<10} {'Low':<10} {'Close':<10} {'Volume':<12}")
            print("-" * 60)
            
            # Show last 10 days
            recent_data = hist.tail(10)
            for date, row in recent_data.iterrows():
                date_str = date.strftime('%Y-%m-%d')
                print(f"{date_str:<12} ${row['Open']:<9.2f} ${row['High']:<9.2f} ${row['Low']:<9.2f} ${row['Close']:<9.2f} {row['Volume']:<12,.0f}")
            
            print()
            
            # Calculate some statistics
            max_price = hist['High'].max()
            min_price = hist['Low'].min()
            avg_price = hist['Close'].mean()
            total_volume = hist['Volume'].sum()
            
            print(f"📊 {period.upper()} STATISTICS")
            print("-" * 30)
            print(f"Highest Price: ${max_price:.2f}")
            print(f"Lowest Price: ${min_price:.2f}")
            print(f"Average Price: ${avg_price:.2f}")
            print(f"Total Volume: {total_volume:,.0f}")
            print()
            
        except Exception as e:
            print(f"❌ Error fetching history for {symbol}: {e}")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("📈 STOCK TRACKER MENU")
        print("=" * 50)
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Stock Details")
        print("5. Price History")
        print("6. Refresh All")
        print("7. Popular Stocks")
        print("8. Market Summary")
        print("9. Auto Refresh (30s)")
        print("0. Exit")
        print("-" * 50)
    
    def show_popular_stocks(self):
        """Show some popular stocks"""
        popular = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX']
        
        print("\n🌟 POPULAR STOCKS")
        print("=" * 80)
        print(f"{'Symbol':<8} {'Price':<12} {'Change':<12} {'Change %':<12}")
        print("-" * 80)
        
        for symbol in popular:
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                change_str = f"${stock_data['change']:+.2f}"
                change_percent_str = f"{stock_data['change_percent']:+.2f}%"
                indicator = "🟢" if stock_data['change'] >= 0 else "🔴"
                
                print(f"{symbol:<8} ${stock_data['price']:<11.2f} {change_str:<12} {change_percent_str:<12} {indicator}")
        print()
    
    def auto_refresh_mode(self):
        """Auto refresh mode - updates every 30 seconds"""
        print("\n🔄 AUTO REFRESH MODE (Press Ctrl+C to stop)")
        print("Refreshing every 30 seconds...")
        
        try:
            while True:
                self.display_portfolio()
                print("⏱️  Next refresh in 30 seconds... (Press Ctrl+C to stop)")
                time.sleep(30)
                self.refresh_all()
        except KeyboardInterrupt:
            print("\n⏹️  Auto refresh stopped")
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        print("🎉 Welcome to Stock Price Tracker!")
        print("Powered by Yahoo Finance API")
        
        # Load some example stocks
        if input("\nWould you like to load some example stocks? (y/n): ").lower() == 'y':
            examples = ['AAPL', 'GOOGL', 'MSFT']
            for symbol in examples:
                self.add_stock(symbol)
        
        while True:
            self.show_menu()
            choice = input("Enter your choice (0-9): ").strip()
            
            if choice == '1':
                symbol = input("Enter stock symbol: ").strip()
                if symbol:
                    self.add_stock(symbol)
                    
            elif choice == '2':
                symbol = input("Enter stock symbol to remove: ").strip()
                if symbol:
                    self.remove_stock(symbol)
                    
            elif choice == '3':
                self.display_portfolio()
                
            elif choice == '4':
                symbol = input("Enter stock symbol for details: ").strip()
                if symbol:
                    self.display_detailed_info(symbol)
                    
            elif choice == '5':
                symbol = input("Enter stock symbol: ").strip()
                if symbol:
                    period = input("Enter period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max) [default: 1mo]: ").strip()
                    if not period:
                        period = "1mo"
                    self.get_price_history(symbol, period)
                    
            elif choice == '6':
                self.refresh_all()
                
            elif choice == '7':
                self.show_popular_stocks()
                
            elif choice == '8':
                # Market summary using major indices
                indices = ['^GSPC', '^DJI', '^IXIC']  # S&P 500, Dow Jones, NASDAQ
                index_names = ['S&P 500', 'Dow Jones', 'NASDAQ']
                
                print("\n📊 MARKET SUMMARY")
                print("=" * 60)
                for i, index in enumerate(indices):
                    data = self.get_stock_data(index)
                    if data:
                        change_str = f"{data['change']:+.2f}"
                        change_percent_str = f"{data['change_percent']:+.2f}%"
                        indicator = "🟢" if data['change'] >= 0 else "🔴"
                        print(f"{index_names[i]:<15} {data['price']:>10,.2f} {change_str:>10} ({change_percent_str}) {indicator}")
                print()
                
            elif choice == '9':
                self.auto_refresh_mode()
                
            elif choice == '0':
                print("👋 Thank you for using Stock Price Tracker!")
                break
                
            else:
                print("❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")


def main():
    """Main function"""
    try:
        tracker = SimpleStockTracker()
        tracker.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
