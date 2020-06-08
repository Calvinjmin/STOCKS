# Reference for tkinter - https://realpython.com/python-gui-tkinter/
# Reference for Login/Register - https://www.youtube.com/watch?v=Xt6SqWuMSA8
import os
from tkinter import *
from termcolor import colored

# REFERENCE STRINGS
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

def is_float(str_value):
    try:
        float(str_value)
        return True
    except ValueError:
        return False

class MainGUI:
    def __init__(self, master, money, portfolio, watch_list):
        ### Window ###

        # Master Window
        self.window = master

        # Login Window
        self.login_screen = Toplevel(self.window)
        self.login_screen.title("Login/Register")
        self.login_screen.geometry("400x400")
        self.login_screen.protocol("WM_DELETE_WINDOW", self.reset_login_screen)
        self.login_screen.withdraw()

        # Login Results Window
        self.login_action_screen = Toplevel(self.window)
        self.login_action_screen.title("Login Result")
        self.login_action_screen.geometry("200x200")
        self.login_action_screen.protocol("WM_DELETE_WINDOW", self.reset_login_result_screen)
        self.login_action_screen.withdraw()

        # Funds Window
        self.funds_screen = Toplevel(self.window)
        self.funds_screen.title("Funds")
        self.funds_screen.geometry("400x400")
        self.funds_screen.protocol("WM_DELETE_WINDOW", self.reset_funds_screen)
        self.funds_screen.withdraw()

        # Versatile Results Screen
        self.result_screen = Toplevel(self.window)
        self.result_screen.title("Results")
        self.result_screen.geometry("200x200")
        self.result_screen.protocol("WM_DELETE_WINDOW", self.reset_results)
        self.result_screen.withdraw()

        ### Frame ###
        self.frame = Frame(master=master)

        ### Import VARS ###
        self.money = money
        self.port = portfolio
        self.wl = watch_list

        ### Variables ###
        self.username = StringVar()
        self.password = StringVar()

        self.session_user = "NA"
        self.login_success = False

        self.funds_entry_str = StringVar()

        ### Widgets ###

        # - Row 0 - #
        self.intro_text = Label(text=intro).grid(row=0, column=0, sticky='nsew', columnspan=5)

        # - Row 1 - #
        self.profile_str = StringVar()
        self.profile_str.set("Current Funds: $" + str(self.money.get_funds()) + "\nCurrent User: " + self.session_user)
        self.funds_text = Label(textvariable=self.profile_str).grid(row=1, column=0, sticky='nsew', columnspan=5)

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
        self.funds_button = Button(text="Funds", command=self.funds_opt)
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

        # - Row 5 - #
        self.login_register_button = Button(text="Login/Register", command=self.login_display)
        self.login_register_button.grid(row=5, column=2, sticky='nsew')

    def set_window_title(self, title):
        self.window.title(title)

    def login_display(self):
        self.login_screen.deiconify()
        Label(self.login_screen, text="Username:").pack()
        Entry(self.login_screen, textvariable=self.username).pack()
        Label(self.login_screen, text="Password:").pack()
        Entry(self.login_screen, textvariable=self.password).pack()
        Button(self.login_screen, text="Login", command=self.login_user).pack()
        Button(self.login_screen, text="Register", command=self.register_user).pack()

    def register_user(self):
        file = open("./users/" + self.username.get(), "w")
        file.write(self.username.get())
        file.write("\n" + self.password.get())
        file.write("\n" + str(0.00))
        file.close()

        self.login_action(1)

    def login_user(self):
        current_user = self.username.get()
        current_password = self.password.get()

        list_of_files = os.listdir(os.path.expanduser('./users/'))
        if current_user in list_of_files:
            file = open("./users/" + current_user, "r")
            verify = file.read().splitlines()
            if current_password in verify:
                self.login_action(2)
            else:
                self.login_action(3)
        else:
            self.login_action(4)

    def login_action(self, action):
        self.login_action_screen.deiconify()
        if action == 1:
            Label(self.login_action_screen, text="Registration Successful", fg="green").pack()
            self.login_success = True
            self.session_user = self.username.get()
            self.update_profile()
            self.reset_login_screen()
        elif action == 2:
            Label(self.login_action_screen, text="Login Successful", fg="green").pack()
            self.login_success = True
            self.session_user = self.username.get()
            self.update_profile()
            self.reset_login_screen()
        elif action == 3:
            Label(self.login_action_screen, text="Password not found", fg="red").pack()
        elif action == 4:
            Label(self.login_action_screen, text="User not found", fg="red").pack()

    def funds_opt(self):
        self.funds_screen.deiconify()
        if self.login_success:
            Label(self.funds_screen, text="Options for Funds").pack()
            Label(self.funds_screen, text="").pack()
            Label(self.funds_screen, text="Type a numerical value to deposit").pack()
            Entry(self.funds_screen, textvariable=self.funds_entry_str).pack()
            Button(self.funds_screen, text="Deposit", command=self.depo_funds).pack()
        else:
            Label(self.funds_screen, text="You are not logged in or registered.", fg="red").pack()

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

    def reset_login_screen(self):
        for widget in self.login_screen.winfo_children():
            widget.destroy()
        self.username.set("")
        self.password.set("")
        self.login_screen.withdraw()

    def reset_login_result_screen(self):
        for widget in self.login_action_screen.winfo_children():
            widget.destroy()
        self.username.set("")
        self.password.set("")
        self.login_action_screen.withdraw()
        self.update_profile()

    def reset_funds_screen(self):
        for widget in self.funds_screen.winfo_children():
            widget.destroy()
        self.funds_entry_str.set("")
        self.funds_screen.withdraw()
        self.update_profile()

    def reset_results(self):
        for widget in self.result_screen.winfo_children():
            widget.destroy()
        self.result_screen.withdraw()

    def port_options(self):
        self.hide_main_widgets()

    def update_profile(self):
        if self.login_success:
            file = open("./users/" + self.session_user, "r")
            file.readline()
            file.readline()
            self.profile_str.set("Current Funds: $" + file.readline() + "\nCurrent User: " + self.session_user)
        else:
            self.profile_str.set(
                "Current Funds: $" + str(self.money.get_funds()) + "\nCurrent User: " + self.session_user)

    def depo_funds(self):
        if is_float(self.funds_entry_str.get()):
            list_of_files = os.listdir(os.path.expanduser('./users/'))
            if self.session_user in list_of_files:
                file = open("./users/" + self.session_user, "r")
                data = file.readlines()
                data[2] = str(float(data[2]) + float(self.funds_entry_str.get()))

                file = open("./users/" + self.session_user, "w")
                file.writelines(data)

                self.result_screen.deiconify()
                Label(self.result_screen,text="Deposit Success",fg="green").pack()

            else:
                print("An error has occurred when reading your profile from the system.")
        else:
            self.funds_entry_str.set("Invalid input")


def main(money, port, watchlist):
    window = Tk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)

    gui = MainGUI(window, money, port, watchlist)
    gui.set_window_title("STOCKS")
    window.mainloop()
