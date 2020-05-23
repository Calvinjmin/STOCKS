import pyfiglet
import platform
import yfinance as yf

# function_mapping = {'1': f.display_portfolio(), '2': f.add_stock(), '3': f.remove_stock()}

option_Display = "\nThe following options are available in this script (Type the number):" \
                 "\n1 - Display the current portfolio with their current market price." \
                 "\n2 - Add a stock to the portfolio." \
                 "\n3 - Remove a stock from the portfolio." \
                 "\nType 'quit' to terminate the program.\n"

condense_Option = "\n1 - Display Portfolio.  2 - Add stock.  " \
                  "\n3 - Remove stock.  'quit' - End Program\n"

# Initializes the script
print(pyfiglet.figlet_format('STOCKS'))
print('Python Version = ' + platform.python_version())
print('Yahoo Finance  = ' + yf.__version__)


def main():
    import func as f
    option = input(option_Display)
    while True:
        if option == 'quit':
            break
        elif option == '1':
            f.display_portfolio()
        elif option == '2':
            f.add_stock()
        elif option == '3':
            f.remove_stock()
        else:
            print("Invalid Input...Try Again\n")
        option = input(condense_Option)


main()
print("Thank you for using my script! - Calvin M.")
