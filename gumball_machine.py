class GumballMachine:
    def __init__(self):
        self.valid_currency = {"nickel": 5, "dime": 10, "quarter": 25}
        # Represents the total value of valid currency the user inserted
        self.currency_value = 0
        self.invalid_currencies = []

    def insert(self, currency):
        # Checks if the inserted value is a valid currency, then adds it
        if currency in self.valid_currency:
            self.currency_value += self.valid_currency[currency]

        # Adds invalid currencies to a list to return it later
        else:
            self.invalid_currencies.append(currency)

    def return_invalid_currency(self):
        response = "Returning your invalid currency of "

        for i in range(len(self.invalid_currencies)):
            response += self.invalid_currencies[i]
            if i < len(self.invalid_currencies) - 1:
                response += ", "

        self.invalid_currencies.clear()

        return response

    def dispense_red(self):
        response = ""

        if self.invalid_currencies:
            response = self.return_invalid_currency()
        else:
            if self.currency_value >= 5:
                self.currency_value -= 5
                response = "Enjoy your red gumball"
            else:
                response = "You need at least 5 cents to dispense a red gumball"

        return response

    def dispense_yellow(self):
        response = ""

        if self.invalid_currencies:
            response = self.return_invalid_currency()
        else:
            if self.currency_value >= 10:
                self.currency_value -= 10
                response = "Enjoy your yellow gumball"
            else:
                response = "You need at least 10 cents to dispense a yellow gumball"

        return response

    def return_my_change(self):
        response = ""

        if self.invalid_currencies:
            response = self.return_invalid_currency()
        else:
            if self.currency_value == 0:
                response = "There is no change to return"
            # Returns the user's change
            else:
                response = f"Returning your change of {self.currency_value} cents"
                self.currency_value = 0

        return response
