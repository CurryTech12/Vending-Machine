def print_stock():
    return ("Stock contains:\n"
            f"   {nickels} nickels\n"
            f"   {dimes} dimes\n"
            f"   {quarters} quarters\n"
            f"   {ones} ones\n"
            f"   {fives} fives\n")


def print_menu():
    return (f"\nMenu for deposits:\n"
            "   'n' - deposit a nickel\n"
            "   'd' - deposit a dime\n"
            "   'q' - deposit a quarter\n"
            "   'o' - deposit a one dollar bill\n"
            "   'f' - deposit a five dollar bill\n"
            "   'c' - cancel the purchase\n")


def get_price():
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    if price == "q":
        total = nickels * 5 + dimes * 10 + quarters * 25 + ones * 100 + fives * 500
        print(f"\nTotal: {int(total / 100)} dollars and {total % 100} cents")
        quit()
    else:
        price = round(float(price) * 100)

    if price <= 0 or price % 5 != 0:
        print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
        return get_price()

    return price


def get_code(price):
    if price > 99:
        print(f"Payment due: {int(price / 100)} dollar(s) and {price % 100} cents")
    else:
        print(f"Payment due: {price % 100} cents")

    code = input("Indicate your deposit: ")
    if code == "n" or code == "d" or code == "q" or code == "o" or code == "f" or code == "c":
        return code

    print(f"Illegal selection: {code}")
    return get_code(price)


def calculate_stock(code, price, original_price):
    global nickels
    global dimes
    global quarters
    global ones
    global fives

    if code == "c":
        price = price - original_price
    elif code == "f":
        price -= 500
        fives += 1
    elif code == "o":
        price -= 100
        ones += 1
    elif code == "q":
        price -= 25
        quarters += 1
    elif code == "d":
        price -= 10
        dimes += 1
    elif code == "n":
        price -= 5
        nickels += 1

    return price


def calculate_change(price):
    global nickels
    global dimes
    global quarters

    out = False
    change_nickels = 0
    change_dimes = 0
    change_quarters = 0

    print("\nPlease take the change below.")
    if price == 0:
        print("  No change due.")
    change = abs(price)
    while change != 0:
        if change >= 25 and quarters > 0:
            change_quarters += 1
            quarters -= 1
            change -= 25
        elif change >= 10 and dimes > 0:
            change_dimes += 1
            dimes -= 1
            change -= 10
        elif change >= 5 and nickels > 0:
            change_nickels += 1
            nickels -= 1
            change -= 5
        else:
            out = True
            break

    if change_quarters > 0:
        print(f"   {change_quarters} quarters")
    if change_dimes > 0:
        print(f"   {change_dimes} dimes")
    if change_nickels > 0:
        print(f"   {change_nickels} nickels")
    if out:
        print(
            f"Machine is out of change.\nSee store manager for reaming refund.\nAmount due is: {int(change / 100)} dollars and {change % 100} cents")
    print()


nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

print("Welcome to the vending machine change maker program\nChange maker initalized.")

while True:
    print(print_stock())
    price = get_price()
    original_price = price
    print(print_menu())

    while price > 0:
        code = get_code(price)
        price = calculate_stock(code, price, original_price)

    calculate_change(price)