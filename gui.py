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


class MainGUI:
    def __init__(self, master, money, portfolio, watch_list):
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
        self.init_options = Label(text=display).grid(row=1, column=0, sticky='w', columnspan=1)

        self.response_str = StringVar()
        self.response_str.set("")
        self.user_response = Entry(textvariable=self.response_str).grid(row=1, column=1, sticky='w')

        self.results_str = StringVar()
        self.results_str.set("")
        self.entry_button = Button(text="Enter", command=self.change_results).grid(row=1, column=2, sticky='w')
        self.results_label = Label(textvariable=self.results_str).grid(row=2, column=0, sticky='nsew', columnspan=3)

    def set_window_title(self, title):
        self.window.title(title)

    def change_results(self):
        text = 'Current Funds: ' + str(self.money.get_funds())
        self.results_str.set(text)

    def add_label_with_pos(self, text, row, column, pos, col_span):
        label = Label(text=text)
        label.grid(row=row, column=column, sticky=pos, columnspan=col_span)

    def add_button_with_pos(self, text, row, column, pos):
        button = Button(text=text)
        button.grid(row=row, column=column, sticky=pos)

    def add_entry_with_pos(self, default_text, row, column, pos):
        entry = Entry(text=default_text)
        entry.grid(row=row, column=column, sticky=pos)


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


if __name__ == '__main__':
    main()
