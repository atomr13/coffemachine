import data


def firstpromt():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        print("turning off")
    elif drink == "report":
        print(f"Water: {data.resources['water']}ml\n"
              f"Milk: {data.resources['milk']}ml\n"
              f"Coffee: {data.resources['coffee']}mg\n")
    else:
        return drink


def sale(choice):
    cost = data.MENU[choice]['cost']
    quar = int(input(f"How many quarters?"))
    dime = int(input(f"How many dimes?"))
    nickel = int(input(f"How many nickels?"))
    penny = int(input(f"How many pennies?"))
    total = 0.25 * quar + 0.1 * dime + 0.05 * nickel + 0.01 * penny
    resultset = {}
    ingre = data.MENU[choice]['ingredients']
    for key in ingre:
        if key in ingre and key in data.resources:
            value1 = ingre[key]
            value2 = data.resources[key]
            if value1 < value2:
                resultset[key] = "lower"
            else:
                resultset[key] = "higher"
    for result in resultset.values():
        if result == 'higher':
            output = "insufficient materials"
        else:
            output = "insert coins"
        if output == "insert coins":
            if total > cost:
                action = f"Enjoy your coffe! Here is your change ${total - cost}"
            elif total == cost:
                action = f"Enjoy your coffee!"
            else:
                action = f"Insufficient funds!"
        print(action)
    if action != f"Insufficient funds!":
        for item, amount in ingre.items():
            data.resources[item] -= amount


sale(firstpromt())
