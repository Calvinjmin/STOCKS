# Reference for tkinter - https://realpython.com/python-gui-tkinter/
from tkinter import *

intro = """Welcome to STOCKS!
        This script will be a simulation of the current stock market."""

display = """The following options are available in this script: 
             1 - Manipulate Portfolio
             2 - Manipulate Funds
             3 - Manipulate a Watch List 
             4 - Info on an individual stock 
             Type 'quit' to terminate the program."""


class MainGUI:
    def __init__(self, master):
        # Window
        self.window = master

        # Frame
        self.frame = Frame(master=master)

    def set_window_title(self, title):
        self.window.title(title)

    def add_label_with_pos(self, text, row, column, pos, col_span):
        label = Label(text=text)
        label.grid(row=row, column=column, sticky=pos, columnspan=col_span)

    def add_button_with_pos(self, text, row, column, pos):
        button = Button(text=text)
        button.grid(row=row, column=column, sticky=pos)

    def add_entry_with_pos(self, default_text, row, column, pos):
        entry = Entry(text=default_text)
        entry.grid(row=row, column=column, sticky=pos)


window = Tk()
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

gui = MainGUI(window)
gui.set_window_title("STOCKS")

gui.add_label_with_pos(intro, 0, 0, 'nsew', 3)
gui.add_label_with_pos(display, 1, 0, 'w', 1)
gui.add_entry_with_pos("", 1, 1, 'w')
gui.add_button_with_pos("Entry", 1, 2, 'w')
gui.add_label_with_pos("Results!", 2, 0, 'nsew', 3)

# PONDER: Efficiency? adding individual widgets or use a class to automate it

window.mainloop()
