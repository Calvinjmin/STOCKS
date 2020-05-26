import stock

wl_display = "\nThe following options are currently available (Type the number):" \
             "\n1 - View current watch list" \
             "\n2 - Add a stock" \
             "\n3 - Remove a stock" \
             "\nType 'return' to go back to the main options.\n"


class Watch_List:
    def __init__(self):
        self.stocks = list(tuple())
        self.name = ""

    def main(self):
        option = input(wl_display)
        while True:
            if option == '1':
                self.print_wl()
            elif option == '2':
                self.add_stock()
            elif option == '3':
                self.remove_stock()
            elif option == 'return':
                return
            option = input(wl_display)


    def get_name(self):
        return self.name

    def print_wl(self):
        if not self.stocks:
            print("The current watch list is empty.")
        else:
            for (ticker, short_name) in self.stocks:
                temp_stock = stock.Stock(ticker)
                print(temp_stock.get_name() + " (" + ticker + ")\nMarket Price: " + str(temp_stock.get_price()))

    def add_stock(self):
        stock_ipt = input("Type in a ticker symbol: ").upper()
        try:
            temp_stock = stock.Stock(stock_ipt)
            short_name = temp_stock.get_name()
            print(short_name + " (" + stock_ipt +") was added to the watch list.")
            self.stocks.append((stock_ipt,short_name))
        except (AttributeError, IndexError) as e:
            print("\nAn error occurred when trying to add " + stock_ipt )

    def remove_stock(self):
        self.print_wl()
        stock_ipt = input("Type in the ticker symbol of the stock you want to remove: ").upper()
        for (ticker,short_name) in self.stocks:
            if ticker == stock_ipt:
                self.stocks.remove((ticker,short_name))
                print(ticker + " has been removed from the watch list.")
                return
