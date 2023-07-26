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
            "coffee": 24
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
}
profit=0

def is_sufficient_resources(drink):
    for item in drink:
        if resources[item] < drink[item]:
            print(f"Sorry not sufficient {item}")
            return False

    return True

def process_coins():
    total = 0
    print("plz insert the coins")
    total = int(input("how many Quarters:"))*0.25
    total += int(input("how many Dimes:")) * 0.1
    total += int(input("how many Nickels:"))*0.05
    total += int(input("how many Pennies:")) * 0.01

    return total

def is_transaction_succesful(drink_cost, money_received):
    if money_received < drink_cost:
        print("Sorry that's not enough money! Money refunded😒")
        return False
    else:
        change = round((money_received - drink_cost),2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is  your {drink_name}, Enjoy👌")

#---------------main----------------
is_on=True
while is_on:
    choice = input("what would you like to order(espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False

    elif choice == "report":
        for item in resources:
            print(f"{item}:{resources[item]}")
    else:
        drink = MENU[choice]
        if is_sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(drink["cost"], payment):
                make_coffee(choice, drink["ingredients"])








