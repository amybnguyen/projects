MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}


def report(resources, money):
    """Returns a summary of resources in the coffee machine."""
    return f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money:.2f}"


def enough_resources(recipe, resources):
    """Returns true if there are sufficient resources in the coffee machine to make a cup of coffee."""
    sufficient_resources = True
    for item in recipe["ingredients"]:
        if recipe["ingredients"][item] > resources[item]:
            sufficient_resources = False
            print(f"Sorry there is not enough {item}.")
    return sufficient_resources


def make_coffee(recipe, resources):
    """Decrease amount of resources according to type of coffee made."""
    resources["water"] -= recipe["ingredients"]["water"]
    resources["milk"] -= recipe["ingredients"]["milk"]
    resources["coffee"] -= recipe["ingredients"]["coffee"]


def collect_money(recipe):
    """Returns true if order can be made and false if not."""
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    pennies = int(input("how many pennies? "))
    amt_paid = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if amt_paid < recipe["cost"]:
        sufficient_money = False
        print("Sorry that's not enough money. Money refunded.")
    else:
        sufficient_money = True
        change = round(amt_paid - recipe["cost"], 2)
        print(f"Here is ${change:.2f} in change.")
    return sufficient_money


def main():
    money = 0
    machine_on = True
    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "off":
            machine_on = False
        elif order == "report":
            print(report(resources, money))
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            if enough_resources(MENU[order], resources):
                if collect_money(MENU[order]):
                    make_coffee(MENU[order], resources)
                    money += MENU[order]["cost"]
                    print(f"Enjoy your {order} ☕!")


main()