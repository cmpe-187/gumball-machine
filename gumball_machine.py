class gumball_machine:
    def __init__(self):
        self.valid_currency = {"nickel": 5, "dime": 10, "quarter": 25}
        self.money_value = 0
        self.money_returned = []

    def insert(self, money):
        if money in self.valid_currency:
            self.money_value += self.valid_currency[money]
        else:
            self.money_returned.append(money)

    def return_invalid_currency(self):
        print("Returning invalid currencies:")
        for x in range(len(self.money_returned)):
            print(self.money_returned[x])

        self.money_returned = []

    def dispense_red(self):
        if len(self.money_returned) != 0:
            self.return_invalid_currency()
        if self.money_value >= 5:
            self.money_value -= 5
            print("Enjoy your red gumball\n")
        else:
            print("You need at least 5 cents to dispense a red gumball\n")

    def dispense_yellow(self):
        if len(self.money_returned) != 0:
            self.return_invalid_currency()
        if self.money_value >= 10:
            self.money_value -= 10
            print("Enjoy your yellow gumball\n")
        else:
            print("You need at least 10 cents to dispense a yellow gumball\n")

    def return_my_change(self):
        if self.money_value == 0:
            print("There is no change to return\n")

        else:
            print("Returning your change of ", self.money_value, " cents")
            self.money_value = 0



