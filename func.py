import yfinance as yf


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
        print(str(stock_name) + ' - ' + str(market_price))

    except Exception:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.')

# Function that retrieves information on the
#   the given ticker symbol in a 5 day period
def print_five_day_period(ticker_symbol):
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        stock_name = ticker_data.info['shortName']
        print(str(ticker_symbol) + ' - ' + str(stock_name))
        print(ticker_data.history(period='5d') )
    except Exception:
        print(str(ticker_symbol) + ' is not a valid ticker symbol in Yahoo Finance.')
