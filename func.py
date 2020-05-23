import yfinance as yf

portfolio = []


# Function that returns the ticker symbol
def print_ticker(ticker_symbol):
    ticker_data = yf.Ticker(ticker_symbol)
    print(ticker_data)


# Function that retrieves the market price
#   for the given ticker symbol
def print_market_price(ticker_symbol):
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        stock_name = ticker_data.info['shortName']
        market_price = ticker_data.info['regularMarketPrice']
        print(str(stock_name) + ' - Market Price: ' + str(market_price))

    except Exception:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.')


# Function that retrieves information on the
#   the given ticker symbol in a 5 day period
def print_five_day_period(ticker_symbol):
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        stock_name = ticker_data.info['shortName']
        print(str(ticker_symbol) + ' - ' + str(stock_name))
        print(ticker_data.history(period='5d'))
    except Exception:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.')


# Adds a given input to the portfolio as a stock.
def add_stock():
    try:
        opt = int(input("How many stocks would you like to enter?\n"))
        for x in range(0, opt):
            stock = input("Please type in a ticker symbol: ")
            if str(stock).upper() in portfolio:
                print(str(stock).upper() + " is already in the portfolio.")
            else:
                portfolio.append(str(stock).upper())
                print(str(stock) + " was added to a temporary portfolio.")
    except ValueError:
        print("The given input was not a number.")


# Removes the given input from the portfolio
def remove_stock():
    stock = input("Please type in a ticker symbol that you want to remove: ")
    try:
        portfolio.remove(str(stock).upper())
        print("Removing " + stock + " was successful!")
    except ValueError:
        print("Removing " + stock + " was unsuccessful.")


# Displays the current portfolio and each stock's market price
def display_portfolio():
    if not portfolio:
        print("The current portfolio is empty.")
    else:
        for stock in portfolio:
            print_market_price(stock)
