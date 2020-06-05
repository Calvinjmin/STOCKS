import yfinance as yf
import matplotlib.pyplot as plt

stock_Display = "\nThe following options are currently available (Type the number):" \
                "\n1 - View the short name of the stock" \
                "\n2 - View the regular market price" \
                "\n3 - Display a graph that shows the profit of the stock in a given period." \
                "\n4 - Display a five day period report of the stock" \
                "\n5 - Query Information online about the stock using the Ticker Symbol." \
                "\nType 'return' to go back to the main options.\n"

class Stock:
    def __init__(self, ticker):
        temp_stock = yf.Ticker(ticker)
        self.ticker = ticker
        self.name = str(temp_stock.info['shortName'])
        self.price = temp_stock.info['regularMarketPrice']

    def stock_main(self):
        option = input(stock_Display)
        while True:
            if option == 'return':
                return
            elif option == '1':
                print('Short Name: ' + self.get_name())
            elif option == '2':
                print('Regular Market Price: $' + str(self.get_price()))
            elif option == '3':
                period = input("Valid input formats - 5d,1mo,3mo,6mo,1y"
                               "\nPlease input a period of time: ")
                self.plot_average(period, self.ticker)
            elif option == '4':
                self.print_five_day_period(self.ticker)
            elif option == '5':
                self.google_search()
            else:
                print("Invalid Input...\n")
            option = input( stock_Display )


    def get_price(self):
        return float(self.price)

    def get_name(self):
        return self.name

        # Function that retrieves information on the given ticker symbol in a 5 day period
    def print_five_day_period(self,ticker_symbol):
        ticker_data = yf.Ticker(ticker_symbol)
        stock_name = ticker_data.info['shortName']
        print(str(ticker_symbol) + ' - ' + str(stock_name))
        print(ticker_data.history(period='5d'))

    # Plots the average value of high and low for a given stock
    def plot_average(self,period,stock):
        ticker = yf.Ticker(stock)
        plot = ((ticker.history(period).get("Close") - ticker.history(period).get("Open")) / 2)
        plt.plot(plot)
        plt.title( stock.upper() )
        plt.xlabel('Date (Year-Month-Day)')
        plt.ylabel('Net Profit (USD)')
        plt.show()

    def google_search(self):
        query = self.ticker
        try:
            from googlesearch import search
        except ImportError:
            print("\n--An error occurred when importing google.--\n")

        print("\nKeyword being search on google: " + query )
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(j)