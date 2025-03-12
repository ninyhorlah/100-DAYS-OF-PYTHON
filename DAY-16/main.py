# from random import choice
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

money_machine = MoneyMachine()
make_coffee = CoffeeMaker()
# order = make_coffee.make_coffee("latte")
get_menu = Menu().find_drink
# print(order)
# print(money_machine.report(), make_coffee.report())


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
        money_machine.report()
    else:
        drink = get_menu(choice)
        if make_coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                make_coffee.make_coffee(drink)
