money_display = "\nThe following options are currently available (Type the number):" \
                "\n1 - Deposit Money" \
                "\nType 'return' to go back to the main options.\n"

class Money:
    def __init__(self):
        self.funds = 0

    def money_main(self):
        option = input(money_display)
        while True:
            if option == '1':
                depo = int(input("\nHow much money would you like to deposit?  "))
                self.deposit(depo)
                self.print_funds()
            elif option == 'return':
                return
            else:
                print("Invalid Input...\n")
            option = input(money_display)

    def print_funds(self):
        print("\n-----CURRENT FUNDS----- " + str(self.funds))

    def get_funds(self):
        return self.funds

    def deposit(self, value):
        self.funds += value