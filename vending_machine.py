products = [
    {
        'Code': 'A1',
        'Name': 'Coca-Cola',
        'Price': 17,
        'Quantity': 5
    },
    {
        'Code': 'A2',
        'Name': 'Coca-Cola-Light',
        'Price': 18,
        'Quantity': 5
    },
    {
        'Code': 'A3',
        'Name': 'Diet-Coke',
        'Price': 20,
        'Quantity': 5
    },
    {
        'Code': 'B1',
        'Name': 'Sprite',
        'Price': 16,
        'Quantity': 5
    },
    {
        'Code': 'B2',
        'Name': 'Fanta',
        'Price': 15,
        'Quantity': 5
    },
    {
        'Code': 'B3',
        'Name': 'Topo-Chico',
        'Price': 22,
        'Quantity': 5
    }
]


def print_options():
    print("Welcome to the vending machine.")
    print("We have the following items available.")
    for i in products:
        print(f"{i['Code']} : {i['Name']} - Price: {i['Price']} - Remaining: {i['Quantity']}")


def input_choice():
    print(
        "Please input your choice and remember this machine accepts 1, 2, 5, 10 pesos coins")
    selection = input("--> ")
    item_choice = None
    code_verification = True
    while code_verification:
        for i in products:
            if i['Code'] == selection:
                print(f"You have selected {i['Name']}.")
                code_verification = False
                item_choice = i
                break
        if code_verification:
            selection = input("Please input a valid code. --> ")
    return item_choice


def print_price(article):
    print(f"Please deposit {article['Price']} pesos.")
    pay_item(article)


def pay_item(article):
    amount = 0
    while amount < article['Price']:
        print(amount)
        coin = verify_amount()
        amount = amount + coin
        print(f"you have paid {amount} pesos.")
        if amount < article['Price']:
            print(f"{article['Price']-amount} still remaining.")
        elif amount == article['Price']:
            print("Exact amount paid.")
        else:
            print(f"{abs(article['Price']-amount)} to be given back.")
    print(f"1 {article['Name']} delivered")


def verify_amount():
    valid_coin = False
    while not valid_coin:
        coin = int(input("--> "))
        if coin == 1 or coin == 2 or coin == 5 or coin == 10:
            return coin
        else:
            print("Please input a valid coin")


def update_stock(update):
    keycode = update['Code']
    for i in products:
        if i['Code'] == keycode:
            i['Quantity'] -= 1


def buy_another() -> bool:
    while True:
        op_status = input("Would you like to buy another? Please input Yes or No.").lower()
        if op_status == 'yes':
            return True
        elif op_status == 'no':
            print("Thank you for buying!")
            return False
        else:
            op_status = input("Please insert a valid response. Yes or No.").lower()


status = True
while status:
    print_options()
    choice = input_choice()
    print_price(choice)
    update_stock(choice)
    status = buy_another()
