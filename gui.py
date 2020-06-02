# Reference for tkinter - https://realpython.com/python-gui-tkinter/

from tkinter import *
import money
import portfolio
import watch_list

intro = """Welcome to STOCKS!
        This script will be a simulation of the current stock market."""

display = """The following options are available in this script: 
             1 - Manipulate Portfolio
             2 - Manipulate Funds
             3 - Manipulate a Watch List 
             4 - Info on an individual stock 
             Type 'quit' to terminate the program."""

portfolio_Display = "\nThe following operations are available (Type the number): " \
                    "\n1 - View your current portfolio. " \
                    "\n2 - Purchase a stock from Yahoo Finance." \
                    "\n3 - Sell a stock from your portfolio." \
                    "\nType 'return' to go back to the main options.\n"

money_display = "\nThe following options are currently available (Type the number):" \
                "\n1 - Deposit Money" \
                "\nType 'return' to go back to the main options.\n"


class MainGUI:
    def __init__(self, master, money, portfolio, watch_list):
        ### Window ###
        self.window = master

        ### Frame ###
        self.frame = Frame(master=master)

        ### Import VARS ###
        self.money = money
        self.port = portfolio
        self.wl = watch_list

        ### Widgets ###

        # - Row 0 - #
        self.intro_text = Label(text=intro).grid(row=0, column=0, sticky='nsew', columnspan=5)

        # - Row 1 - #
        self.funds_str = StringVar()
        self.funds_str.set("Current Funds: $" + str(money.get_funds()))
        self.funds_text = Label(textvariable=self.funds_str).grid(row=1, column=0, sticky='nsew', columnspan=5)

        # - Row 2 - #
        self.type_display_str = StringVar()
        self.type_display_str.set("Main Display")
        self.type_display = Label(textvariable=self.type_display_str).grid(row=2, column=0, sticky='nsew', columnspan=5)

        # - Row 3 - #
        # Main Menu Button
        self.reset_button = Button(text="Main Menu", command=self.reset_gui)
        self.reset_button.grid(row=3, column=0)

        # Portfolio Button
        self.portfolio_button = Button(text="Portfolio")
        self.portfolio_button.grid(row=3, column=1)

        # Funds Button
        self.funds_button = Button(text="Funds")
        self.funds_button.grid(row=3, column=2)

        # Watch List Button
        self.wl_button = Button(text="Watch Lists")
        self.wl_button.grid(row=3, column=3)

        # Stock Info. Button
        self.stock_info_button = Button(text="Indv. Stock")
        self.stock_info_button.grid(row=3, column=4)

        # - Row 4 - #
        # Portfolio Label
        self.port_str = StringVar()
        self.port_str.set("Manipulate your the portfolio.")
        self.port_message = Label(textvariable=self.port_str)
        self.port_message.grid(row=4, column=1)

        # Funds Label
        self.funds_str = StringVar()
        self.funds_str.set("Access options to your funds.")
        self.funds_message = Label(textvariable=self.funds_str)
        self.funds_message.grid(row=4, column=2)

        # Watch List Label
        self.wl_str = StringVar()
        self.wl_str.set("Manipulate your watch lists.")
        self.wl_message = Label(textvariable=self.wl_str)
        self.wl_message.grid(row=4, column=3)

        # Stock Info. Label
        self.stock_info_str = StringVar()
        self.stock_info_str.set("Access info. about a single stock.")
        self.stock_info_message = Label(textvariable=self.stock_info_str)
        self.stock_info_message.grid(row=4, column=4)

        ### Option Widgets ###
        ## UPCOMING CHANGES

    def set_window_title(self, title):
        self.window.title(title)

    def hide_main_widgets(self):
        self.portfolio_button.grid()
        self.port_message.grid_remove()

        self.funds_button.grid_remove()
        self.funds_message.grid_remove()

        self.wl_button.grid_remove()
        self.wl_message.grid_remove()

        self.stock_info_button.grid_remove()
        self.stock_info_message.grid_remove()

    def reset_gui(self):
        self.type_display_str.set("Main Display")

        # Restore Buttons and Text
        self.portfolio_button.grid()
        self.port_message.grid()

        self.funds_button.grid()
        self.funds_message.grid()

        self.wl_button.grid()
        self.wl_message.grid()

        self.stock_info_button.grid()
        self.stock_info_message.grid()

    def port_options(self):
        self.hide_main_widgets()

    def update_funds(self):
        # Updates the Current Funds str
        text = "Current Funds: $" + str(self.money.get_funds())
        self.funds_str.set(text)


def main(money, port, watchlist):
    window = Tk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)

    gui = MainGUI(window, money, port, watchlist)
    gui.set_window_title("STOCKS")
    window.mainloop()
