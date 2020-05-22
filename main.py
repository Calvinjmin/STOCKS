import pyfiglet
import platform
import yfinance as yf
import func as f

portfolio = []

# Initializes the script
print(pyfiglet.figlet_format('STOCKS'))
print('Python Version = ' + platform.python_version())
print('Yahoo Finance  = ' + yf.__version__)

# User input for Stocks
while True:
    stock = input("Please type in a ticker symbol or enter 'quit': ")
    if stock == 'quit':
        break
    portfolio.append(str(stock).upper())
    print(str(stock) + " was added to a temporary portfolio.")

# Checks to see if the current portfolio is empty
if not portfolio:
    print('The current portfolio is empty. The script will now end.')
else:
    print('\n-----Current Market Prices-----')
    for stock in portfolio:
        f.print_market_price(stock)
    print('\n-----5 Day Period-----')
    for stock in portfolio:
        f.print_five_day_period(stock)