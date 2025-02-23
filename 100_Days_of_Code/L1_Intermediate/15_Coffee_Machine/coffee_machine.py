MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 100
}

coins = {
    "quarter": .25,
    "dime": .10,
    "nickel": .05,
    "penny": .01
}

machine_state = "on"

while machine_state == "on":
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off".lower():
        machine_state = "off"
        break
    elif coffee == "report".lower():
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
        continue
    elif coffee not in MENU:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
        continue
    insufficient = False
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if ingredient in resources and resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            insufficient = True
            break
    if insufficient:
        continue
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = ((quarters * coins["quarter"]) + (dimes * coins["dime"]) + (nickels * coins["nickel"])
             + (pennies * coins["penny"]))
    if total >= MENU[coffee]["cost"]:
        change = total - MENU[coffee]["cost"]
        resources["money"] += MENU[coffee]["cost"]
        for ingredient, amount in MENU[coffee]["ingredients"].items():
            resources[ingredient] -= amount
        if change > 0:
            print(f"Here is your change: ${change}")
        print(f"Here is your {coffee} ☕️ Enjoy!")
    else:
        print(f"Sorry, that's not enough money. Money refunded")
