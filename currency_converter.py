menu = {
    1: 'From ETB to Other Currency',
    2: 'From Other Currency to ETB',
    3: 'Exit'
}

other_currency = {
    1: ' Canadian Dollar',
    2: ' South African Rand',
    3: ' Pound Sterling',
    4: ' Australian Dollar',
    5: ' US Dollar',
    6: ' Saudi Riyal',
    7: ' EURO',
    8: ' Swiss Franc',
    9: ' Kenyan Shilling',
    10: ' Swedish Kroner'
}

rate = {
    1: '35.717',
    2: '2.9599',
    3: '57.0801',
    4: '31.7730',
    5: '52.5494',
    6: '12.6529',
    7: '52.4180',
    8: '51.9134',
    9: '0.4356',
    10: '4.3969'
}


def currency_check(choice, check):
    if check == 1:
        if choice > 10:
            print('Wrong Input:', choice, 'please try again ...')
            choice = int(input("\nPlease Choose: "))
            currency_check(choice, check)
        else:
            ETB = float(input("Enter the amount you want to convert (ETB): "))
            currency_calc(ETB, check, choice)
    else:
        if choice > 10:
            print('Wrong Input:', choice, 'please try again ...')
            choice = int(input("\nPlease Choose: "))
            currency_check(choice, check)
        else:
            Other = float(
                input("Enter the amount you want to convert ("+other_currency[choice]+"): "))
            currency_calc(Other, check, choice)


def currency_calc(amount, check, choice):
    if check == 1:
        for i in other_currency.keys():
            if i == choice:
                converted = amount/float(rate[i])
                print(amount, "ETB will be ", converted, " ",
                      other_currency[i], "in today's market")
    else:
        for i in other_currency.keys():
            if i == choice:
                converted = float(rate[i])*amount
                print(amount, other_currency[i], "will be ",
                      converted, "ETB ", "in today's market")


def welcome_page():
    print("\n----------- Welcome to Ge'ez Currency Converter -----------\n")
    for key in menu.keys():
        print("\t", key, '-', menu[key])


def ETB_to_Others():
    check = 1
    print("To what currency do you want to convert the ETB\n")

    for key in other_currency.keys():
        print("\t", key, '-', other_currency[key])

    choice = int(input("\nPlease Choose: "))
    currency_check(choice, check)


def Others_to_ETB():
    check = 2
    print("From what currency do you want to convert to ETB\n")

    for key in other_currency.keys():
        print("\t", key, '-', other_currency[key])

    choice = int(input("\nPlease Choose: "))
    currency_check(choice, check)


while (True):

    welcome_page()

    option = ""

    option = int(input("\nPlease choose one of the two options: "))
    
    if option == 1:
        ETB_to_Others()

    elif option == 2:
        Others_to_ETB()

    elif option == 3:
        print("Exit code....")
        exit()
    else:
        print('Wrong Input:', option, 'please try again ...')
