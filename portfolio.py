import stock

# Variable for the text displayed when portfolio.py is initialized
portfolio_Display = "\nThe following operations are available (Type the number): " \
                    "\n1 - View your current portfolio. " \
                    "\n2 - Purchase a stock from Yahoo Finance." \
                    "\n3 - Sell a stock from your portfolio." \
                    "\nType 'return' to go back to the main options.\n"


class Portfolio:
    def __init__(self, money):
        self.port = list(tuple())
        self.money = money

    def main(self):
        self.money.print_funds()
        option = input(portfolio_Display)
        while True:
            if option == '1':
                self.print_portfolio()
            elif option == '2':
                ticker = input('What is the ticker symbol of your desired stock? ').upper()
                amount = input('How many shares of ' + ticker + ' would you like to purchase?  ')
                self.purchase_stock(ticker, amount)
            elif option == '3':
                ipt = input("Would you like to see your current portfolio? (Y/N)  ").upper()
                if ipt == 'Y':
                    self.print_portfolio()
                ticker_ipt = input("Please type the ticker symbol of a stock. ").upper()
                amount_ipt = input("How many shares of " + ticker_ipt + " would you like to sell? ")
                self.sell_stock(ticker_ipt, amount_ipt)
            elif option == 'return':
                return
            else:
                print("Invalid Input...\n")
            option = input(portfolio_Display)

    def print_portfolio(self):
        if not self.port:
            print("--The current portfolio is empty--")
        else:
            print("\n---Current Portfolio---")
            for (name, ticker_name, amount) in self.port:
                print(ticker_name + " (" + ticker_name + ") Amount: " + amount)

    def purchase_stock(self, ticker, amount):
        current_funds = self.money.get_funds()
        try:
            s = stock.Stock(ticker)
            if (s.get_price() * float(amount)) <= float(current_funds):
                option = input("\nThe total amount will be " + str(
                    s.get_price() * float(amount)) + " and your current funds are " + str(current_funds) +
                               "\nAre you sure you want to continue with your purchase?\nType (Y/N)  -  ").upper()
                if option == 'Y':
                    self.money.deposit(-(s.get_price() * float(amount)))
                    self.port.append((str(s.get_name()).upper(), ticker, amount))
                elif option == 'N':
                    print("You did NOT complete the transaction.")
                else:
                    print("Invalid input...\n")
            else:
                print("\n!!!Current funds will not allow you to purchase this stock.!!!"
                      "\nThe total amount will be " + str(
                    s.get_price() * float(amount)) + " and your current funds are " + str(current_funds))
        except (AttributeError, IndexError) as e:
            print("\n!!!Invalid Stock!!!")

    def sell_stock(self, ticker, amount):
        for idx, (port_name, port_ticker, stock_amount) in enumerate(self.port):
            if port_ticker == ticker:
                if amount > stock_amount:
                    print("The amount you are trying to sell is more than the portfolio amount.")
                    return
                else:
                    temp_stock = stock.Stock(port_ticker)
                    if amount == stock_amount:
                        self.port.remove((port_name,port_ticker,stock_amount))
                        self.money.deposit(temp_stock.get_price() * float(amount))
                        print("You sold " + str(amount) + " shares of " + ticker
                            + ". " + str(temp_stock.get_price() * float(amount)) + " was added to your current funds.")
                        return
                    else:
                        temp_list = list(self.port[idx])
                        temp_list[2] = str(int(stock_amount) - int(amount))
                        self.port[idx] = temp_list

                        self.money.deposit(temp_stock.get_price() * float(amount))
                        print("You sold " + str(amount) + " shares of " + ticker
                              + ". " + str(temp_stock.get_price() * float(amount)) + " was added to your current funds.")
                        return
        print("The given ticker symbol (" + ticker + ") was not found in the current portfolio.")
