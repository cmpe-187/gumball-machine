valid_currency = {"nickel": 5, "dime": 10, "quarter": 25}

money_inserted = []
money_value = 0
money_returned = []

def insert(money):
    money_inserted.append(money)

def convert_currency():
    current_value = 0
    for x in range(len(money_inserted) - 1):
        if money_inserted[x] in valid_currency:
            current_value += valid_currency[money_inserted[x]]
        else:
            money_returned.append(money_inserted[x])

    return current_value

def dispense_red(money_value):
    if money_value == 0:
        money_value = convert_currency()
    
