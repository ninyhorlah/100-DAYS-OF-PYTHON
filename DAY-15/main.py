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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

should_continue = True


def water_resources():
    return resources["water"]


def milk_resources():
    return resources["milk"]


def coffee_resources():
    return resources["coffee"]


money_made = 0


def process_coin(coffee):
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    customer_coins = (
        (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    )
    coffee_choice_amount = MENU[coffee]["cost"]
    change_left = round((customer_coins - coffee_choice_amount), 1)

    if customer_coins < coffee_choice_amount:
        print("Sorry that's not enough money. Money refunded.")
    elif customer_coins == coffee_choice_amount:
        print(f"Here is your {coffee}. Enjoy!")
    else:
        print(f"The total money you paid is ${round(customer_coins, 1)}")
        print(f"You bought coffee worth ${coffee_choice_amount}")
        print(f"Here is ${change_left} in change")
        print(f"Here is your {coffee} ☕️. Enjoy!")
        global money_made
        money_made += coffee_choice_amount


def not_enough_resource(
    customer_coffee, requested_water=0, requested_coffee=0, requested_milk=0
):
    if requested_water > water_resources():
        print("Sorry, not enough water.")
        print(
            f"Available water {resources['water']}ml, Water requested: {requested_water}ml"
        )
        return
    elif requested_coffee > coffee_resources():
        print("Sorry, not enough coffee.")
        print(
            f"Available coffee {resources['coffee']}g, coffee requested: {requested_coffee}g"
        )
        return
    elif requested_milk > milk_resources():
        print("Sorry, not enough milk.")
        print(
            f"Available milk {resources['milk']}ml, milk requested: {requested_milk}ml"
        )
        return
    else:
        resources["water"] -= requested_water
        resources["coffee"] -= requested_coffee
        resources["milk"] -= requested_milk
        process_coin(customer_coffee)


def espresso():
    ingredients = MENU["espresso"]["ingredients"]
    espresso_water = ingredients["water"]
    espresso_coffee = ingredients["coffee"]
    not_enough_resource("espresso", espresso_water, espresso_coffee)


def latte():
    ingredients = MENU["latte"]["ingredients"]
    latte_water = ingredients["water"]
    latte_coffee = ingredients["coffee"]
    latte_milk = ingredients["milk"]
    not_enough_resource("latte", latte_water, latte_coffee, latte_milk)


def cappuccino():
    ingredients = MENU["cappuccino"]["ingredients"]
    cappuccino_water = ingredients["water"]
    cappuccino_coffee = ingredients["coffee"]
    cappuccino_milk = ingredients["milk"]
    not_enough_resource(
        "cappuccino", cappuccino_water, cappuccino_coffee, cappuccino_milk
    )


while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "latte":
        latte()

    elif order == "espresso":
        espresso()

    elif order == "cappuccino":
        cappuccino()

    elif order == "report":
        water = resources["water"]
        coffee = resources["coffee"]
        milk = resources["milk"]

        print(
            f"Water: {water}ml\nCoffee: {coffee}g\nMilk: {milk}ml\nMoney: ${money_made}"
        )

    elif order == "off":
        print("The program has now been shut down.")
        should_continue = False
