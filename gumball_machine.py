class GumballMachine:
    def __init__(self):
        self.valid_currency = {"nickel": 5, "dime": 10, "quarter": 25}
        # Represents the total value of valid currency the user inserted
        self.money_value = 0
        self.invalid_currencies = []

    def insert(self, money):
        # Checks if the inserted value is a valid currency then adds it
        if money in self.valid_currency:
            self.money_value += self.valid_currency[money]

        # Adds invalid currencies to a list to return it later
        else:
            self.invalid_currencies.append(money)

    def return_invalid_currency(self):
        print("Returning invalid currencies:")
        for x in range(len(self.invalid_currencies)):
            print(self.invalid_currencies[x])

        self.money_returned = []

    def dispense_red(self):
        # Checks if there are any invalid currencies
        if len(self.invalid_currencies) != 0:
            self.return_invalid_currency()

        if self.money_value >= 5:
            self.money_value -= 5
            return "Enjoy your red gumball"

        else:
            return "You need at least 5 cents to dispense a red gumball"

    def dispense_yellow(self):
        if len(self.invalid_currencies) != 0:
            self.return_invalid_currency()

        if self.money_value >= 10:
            self.money_value -= 10
            return "Enjoy your yellow gumball"

        else:
            return "You need at least 10 cents to dispense a yellow gumball"

    def return_my_change(self):
        if self.money_value == 0:
            return "There is no change to return"

        # Returns the user's change
        else:
            self.money_value = 0
            return "Returning your change of ", self.money_value, " cents"
