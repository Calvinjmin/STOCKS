import yfinance as yf
import matplotlib.pyplot as plt

portfolio = []
stock_Display = "\nThe following options are currently available (Type the number):" \
                "\n1 - Display a graph that shows the profit of the stock in a given period." \
                "\n2 - Display a five day period report of the stock" \
                "\n3 - View the website url for the stock." \
                "\nType 'change' to modify the current stock" \
                "\nType 'return' to leave these options\n"

# NOTE: longBusinessSummary, website
def indv():
    display_ticker()
    if not portfolio:
        print("Please add at least one stock to your portfolio to access more functions.")
        return
    else:
        stock_name = input("Please type in a ticker symbol from your portfolio to view more about it - ").upper()
        while True:
            print("\nViewing options for the current stock: " + str(stock_name).upper())
            option = input(stock_Display)
            if option == 'return':
                return
            elif option == 'change':
                display_ticker()
                stock_name = input("Please type in a ticker symbol from your portfolio to view more about it - ").upper()
            elif option == '1':
                period = input("Valid input formats - 5d,1mo,3mo,6mo,1y"
                               "\nPlease input a period of time: ")
                plot_average(period,stock_name)
            elif option == '2':
                print_five_day_period(stock_name)
            elif option == '3':
                display_website(stock_name)


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
    except IndexError:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.'
                                   '\n  Or the given ticker symbol is not supported by this API.')

# Function that retrieves information on the
#   the given ticker symbol in a 5 day period
def print_five_day_period(ticker_symbol):
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        stock_name = ticker_data.info['shortName']
        print(str(ticker_symbol) + ' - ' + str(stock_name))
        print(ticker_data.history(period='5d'))
    except IndexError:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.'
                                   '\n  Or the given ticker symbol is not supported by this API.')

def display_website(ticker_symbol):
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        print( ticker_symbol + " - " + ticker_data.info['website'] )
    except IndexError:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.'
                                   '\n  Or the given ticker symbol is not supported by this API.')

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
                print(str(stock).upper() + " was added to your temporary portfolio.")
    except ValueError:
        print("The given input was not a number.")


# Removes the given input from the portfolio
def remove_stock():
    display_ticker()
    stock = input("Please type in a ticker symbol that you want to remove: ")
    try:
        portfolio.remove(str(stock).upper())
        print("Removing " + str(stock).upper()+ " was successful!")
    except ValueError:
        print("Removing " + str(stock).upper() + " was unsuccessful.")

# Displays all the stocks in the current portfolio
def display_ticker():
    if not portfolio:
        print("\n***The current portfolio is empty***")
    else:
        print("\nThe following ticker symbols are in the current portfolio:")
        for stock in portfolio:
            print(stock)

# Displays the current portfolio and each stock's market price
def display_portfolio():
    if not portfolio:
        print("The current portfolio is empty.")
    else:
        for stock in portfolio:
            print_market_price(stock)

# Displays the average value of each stock given a period of time
def calc_average(period):
    for stock in portfolio:
        ticker = yf.Ticker(stock)
        print(ticker)
        print((ticker.history(period).get("Close") - ticker.history(period).get("Open")) / 2)

# Plots the average value of high and low for a given stock
def plot_average(period,stock):
    ticker = yf.Ticker(stock)
    plot = ((ticker.history(period).get("Close") - ticker.history(period).get("Open")) / 2)
    plt.plot(plot)
    plt.title( stock.upper() )
    plt.xlabel('Date (Year-Month-Day)')
    plt.ylabel('Net Profit (USD)')
    plt.show()
