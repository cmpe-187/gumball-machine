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

    def dispense_red(self):
        if self.money_value >= 5:
            self.money_value -= 5
        else:
            print("You need at least 5 cents to dispense a red gumball\n")

    def dispense_yellow(self):
        if self.money_value >= 10:
            self.money_value -= 10
        else:
            print("You need at least 10 cents to dispense a red gumball\n")





