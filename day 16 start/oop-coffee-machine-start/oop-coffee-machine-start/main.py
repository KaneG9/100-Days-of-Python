from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()


def start_machine():
    order = input("What would you like? (espresso/latte/cappuccino/):")
    if order == 'off':
        return
    elif order == 'report':
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
    return start_machine()


start_machine()
