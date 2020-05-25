money_display = """"The following options are currently available (Type the number):" 
                "1 - Deposit Money" 
                "2 - Withdraw Money"""


class Money:
    def __init__(self):
        self.funds = 0

    def money_main(self):
        print(self.funds)
        value = input("value: ")
        self.funds = self.funds + int(value)
        print(self.funds)

    def display_funds(self):
        return "\n-----CURRENT FUNDS----- " + str(self.funds)

    """"
    option = input(money_display)
    if option == '1':
        deposit()
    elif option == '2':
        print("Withdraw")
    else:
        print(str(money) + "Testing import")
    """
