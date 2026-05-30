# 1. take input about coffee

def welcome():
    global response
    response = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

# 2. initialize every components
working = True
Milk = 200
Water = 300
Coffee = 100  # ✅ fixed from -100
Money = 0

def report():
    print(f"Milk : {Milk}ml | Water : {Water}ml | Coffee : {Coffee}g | Money : ${Money}")

def wanna_continue():
    global working
    output = str(input("Wanna continue? Y or N: ")).lower()  # ✅ fixed .lower()
    if output == "y":
        working = True
    else:
        working = False

def coins_calcu():
    print("Please insert coins.")
    x = int(input("Enter number of quarters: "))
    y = int(input("Enter number of dimes: "))
    z = int(input("Enter number of nickels: "))
    w = int(input("Enter number of pennies: "))
    total = (x * 0.25) + (y * 0.10) + (z * 0.05) + (w * 0.01)
    return total  # ✅ returning instead of using global


while working:
    welcome()

    if response == "report":
        report()

    elif response == "off":
        print("Shutting down. Goodbye!")
        working = False

    elif response == "espresso":
        if Water < 50:
            print("Sorry, not enough water.")
        elif Coffee < 18:
            print("Sorry, not enough coffee.")
        else:
            print("TOTAL IS $1.5. PLEASE INSERT COINS")
            total = coins_calcu()  # ✅ capturing returned value
            if total < 1.5:
                print("Not enough money. Refunding.")
            elif total > 1.5:
                change = round(total - 1.5, 2)  # ✅ round() to avoid float weirdness
                print(f"Here is ${change} in change.")
                Water -= 50
                Coffee -= 18
                Money += 1.5
                print("Here is your espresso ☕ Enjoy!")
            else:
                Water -= 50
                Coffee -= 18
                Money += 1.5
                print("Here is your espresso ☕ Enjoy!")
            wanna_continue()

    elif response == "latte":
        if Water < 200:
            print("Sorry, not enough water.")
        elif Coffee < 24:
            print("Sorry, not enough coffee.")
        elif Milk < 150:
            print("Sorry, not enough milk.")
        else:
            print("TOTAL IS $2.5. PLEASE INSERT COINS")
            total = coins_calcu()
            if total < 2.5:
                print("Not enough money. Refunding.")
            elif total > 2.5:
                change = round(total - 2.5, 2)
                print(f"Here is ${change} in change.")
                Water -= 200
                Coffee -= 24
                Milk -= 150
                Money += 2.5
                print("Here is your latte ☕ Enjoy!")
            else:
                Water -= 200
                Coffee -= 24
                Milk -= 150
                Money += 2.5
                print("Here is your latte ☕ Enjoy!")
            wanna_continue()

    elif response == "cappuccino":
        if Water < 250:
            print("Sorry, not enough water.")
        elif Coffee < 24:
            print("Sorry, not enough coffee.")
        elif Milk < 100:
            print("Sorry, not enough milk.")
        else:
            print("TOTAL IS $3.0. PLEASE INSERT COINS")
            total = coins_calcu()
            if total < 3.0:
                print("Not enough money. Refunding.")
            elif total > 3.0:
                change = round(total - 3.0, 2)
                print(f"Here is ${change} in change.")
                Water -= 250
                Coffee -= 24
                Milk -= 100
                Money += 3.0
                print("Here is your cappuccino ☕ Enjoy!")
            else:
                Water -= 250
                Coffee -= 24
                Milk -= 100
                Money += 3.0
                print("Here is your cappuccino ☕ Enjoy!")
            wanna_continue()

    else:
        print("Invalid choice! Please choose espresso, latte, or cappuccino.")  # ✅ handles bad input