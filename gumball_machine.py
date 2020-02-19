class gumball_machine:
    def __init__(self):
        self.valid_currency = {"nickel": 5, "dime": 10, "quarter": 25}
        self.money_inserted = []
        self.money_value = 0
        self.money_returned = []

    def insert(self, money):
        self.money_inserted.append(money)

    def convert_currency(self):
        for x in range(len(self.money_inserted) - 1):
            if self.money_inserted[x] in self.valid_currency:
                self.money_value += self.valid_currency[self.money_inserted[x]]
            else:
                self.money_returned.append(self.money_inserted[x])

    def dispense_red(self):
        if self.money_value == 0:
            self.convert_currency()



