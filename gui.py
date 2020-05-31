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


def represents_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


class MainGUI:
    def __init__(self, master, money, portfolio, watch_list):
        # 0 - Display, 1 - Portfolio Display, 2 - Money Display
        self.type_display = 0

        # Window
        self.window = master

        # Frame
        self.frame = Frame(master=master)

        # Import VARS
        self.money = money
        self.port = portfolio
        self.wl = watch_list

        # Widgets
        self.intro_text = Label(text=intro).grid(row=0, column=0, sticky='nsew', columnspan=3)

        self.display_str = StringVar()
        self.display_str.set(display)
        self.init_options = Label(textvariable=self.display_str).grid(row=2, column=0, sticky='w', columnspan=1)

        self.funds_str = StringVar()
        self.funds_str.set("Current Funds: $" + str(money.get_funds()))
        self.funds_text = Label(textvariable=self.funds_str).grid(row=1, column=0, sticky='nsew', columnspan=3)

        self.response_str = StringVar()
        self.response_str.set("")
        self.user_response = Entry(textvariable=self.response_str).grid(row=2, column=1, sticky='w')

        self.results_str = StringVar()
        self.results_str.set("")
        self.entry_button = Button(text="Enter", command=self.change_results).grid(row=2, column=2, sticky='w')
        self.results_label = Label(textvariable=self.results_str).grid(row=3, column=0, sticky='nsew', columnspan=3)

    def set_window_title(self, title):
        self.window.title(title)

    def change_results(self):
        if self.type_display == 0:
            self.update_display()
        elif self.type_display == 2:
            self.update_funds()

        # Updates the Current Funds str
        text = "Current Funds: $" + str(self.money.get_funds())
        self.funds_str.set(text)

        # Updates the result/response str
        self.results_str.set("Option Selected - " + str(self.response_str.get()))
        self.response_str.set("")

    def update_display(self):
        if self.response_str.get() == '1' or 'Manipulate Portfolio':
            self.display_str.set(portfolio_Display)
        elif self.response_str.get() == '2' or 'Manipulate Funds':
            self.display_str.set(money_display)
        else:
            self.display_str.set(display)

    def update_funds(self):

        """"
        if self.response_str.get() == '1' or 'Deposit Money':
            while True:
                if represents_int(self.response_str.get()):
                    self.money.deposit(int(self.response_str.get()))
                    self.display_str.set(display)
                    self.type_display = 0
        """




def main(money, port, watchlist):
    window = Tk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    gui = MainGUI(window, money, port, watchlist)
    gui.set_window_title("STOCKS")
    window.mainloop()

"""    def add_label_with_pos(self, text, row, column, pos, col_span):
        label = Label(text=text)
        label.grid(row=row, column=column, sticky=pos, columnspan=col_span)

    def add_button_with_pos(self, text, row, column, pos):
        button = Button(text=text)
        button.grid(row=row, column=column, sticky=pos)

    def add_entry_with_pos(self, default_text, row, column, pos):
        entry = Entry(text=default_text)
        entry.grid(row=row, column=column, sticky=pos) """

