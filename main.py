import pyfiglet
import platform
import money
import yfinance as yf
import func as f


option_Display = "\nThe following options are available in this script (Type the number):" \
                 "\n1 - Display the current portfolio with their current market price." \
                 "\n2 - Add a stock to the portfolio." \
                 "\n3 - Remove a stock from the portfolio." \
                 "\n4 - View the profit of each stock given a period of time.\n" \
                 "\nType '$' to access functions that manipulate your current funds." \
                 "\nType 'indv' to access specific functions." \
                 "\nType 'quit' to terminate the program.\n"

condense_Port_Display = "1 - Display Portfolio.  2 - Add stock.  " \
                        "\n3 - Remove stock.  4 - View profits" \
                        "\n'indv' - Specific Functions  '$' - Funds" \
                        "\n'quit' - End Program\n"

# Initializes the script
print(pyfiglet.figlet_format('STOCKS'))
print('Python Version = ' + platform.python_version())
print('Yahoo Finance  = ' + yf.__version__)


def main():
    m = money.Money()
    print(m.display_funds())
    option = input(option_Display)
    while True:
        if option == 'quit':
            break
        elif option == 'indv':
            f.indv()
        elif option == '$':
            m.money_main()
        elif option == '1':
            f.display_portfolio()
        elif option == '2':
            f.add_stock()
        elif option == '3':
            f.remove_stock()
        elif option == '4':
            period = input("Valid input formats - 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max"
                           "\nPlease input a period of time: ")
            f.calc_average(period)
        else:
            print("Invalid Input...Try Again\n")
        print( m.display_funds())
        option = input(condense_Port_Display)


main()
print("Thank you for using my script! - Calvin M.")

# function_mapping = {'1': f.display_portfolio(), '2': f.add_stock(), '3': f.remove_stock()}
