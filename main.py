import pyfiglet
import platform
import money
import yfinance as yf
import portfolio
import stock
import watch_list
import gui

display = "The following options are available in this script (Type the number): " \
          "\n1 - Manipulate Portfolio" \
          "\n2 - Manipulate Funds" \
          "\n3 - Manipulate a Watch List" \
          "\n4 - Information about an individual stock" \
          "\nType 'quit' to terminate the program." \
          "\nType 'gui' to use the GUI Version!\n"

# Initializes the script
print(pyfiglet.figlet_format('STOCKS'))
print('Python Version = ' + platform.python_version())
print('Yahoo Finance  = ' + yf.__version__)


def main():
    # Initialize Variables (Imports)
    m = money.Money()
    port = portfolio.Portfolio(m)
    wl = watch_list.Watch_List()

    # Main Text Display
    m.print_funds()
    option = input(display)

    while True:
        if option == '1':
            port.main()
        elif option == '2':
            m.money_main()
        elif option == '3':
            wl.main()
        elif option == '4':
            ipt = input("Would you like to see your current portfolio? (Y/N)  ").upper()
            if ipt == 'Y':
                port.print_portfolio()
            ipt = input("Would you like to see your current watch list? (Y/N)  ").upper()
            if ipt == 'Y':
                wl.print_wl()
            stock_ipt = input("Please type the ticker symbol of a stock.  ").upper()
            try:
                stock.Stock(stock_ipt).stock_main()
            except (AttributeError, IndexError, KeyError) as e:
                print("\n" + str(stock_ipt) + ' is not a valid ticker symbol in Yahoo Finance '
                                              'or the given ticker symbol is not supported by the yfinance API.')
        elif option == 'gui':
            gui.main(m,port,wl)
            print("This feature has not been implemented yet!")
        elif option == 'quit':
            return
        m.print_funds()
        option = input(display)


if __name__ == '__main__':
    main()
    print("Thank you for using my script! - Calvin M.")
