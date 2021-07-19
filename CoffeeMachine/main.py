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
}


class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.money = 0

    def check_resources(self, order):
        for ingredient, amount in MENU[order]["ingredients"].items():
            if resources[ingredient] < amount:
                return ingredient
        return True

    def take_coins(self):
        print('Please insert coins.')
        quarters = input("Quarters:")
        dimes = input("Dimes:")
        nickels = input("Nickels:")
        return int(quarters or 0) * 0.25 + int(dimes or 0) * 0.1 + int(nickels or 0) * 0.01

    def complete_transaction(self, order, money_in):
        self.money += MENU[order]['cost']
        change = money_in - MENU[order]['cost']
        for ingredient, amount in MENU[order]["ingredients"].items():
            self.resources[ingredient] -= MENU[order]["ingredients"][ingredient]
        if change != 0: print(f"Here is ${change:.2f} in change.")
        return f"Here is your {order}. Enjoy!"

    def process_order(self, order):
        availability = self.check_resources(order)
        if isinstance(availability, str):
            return f'Sorry there is not enough {availability}.'
        else:
            total = self.take_coins()
            if total < MENU[order]['cost']:
                return "Sorry that's not enough money. Money refunded."
            else:
                return self.complete_transaction(order, total)

    def turn_on(self):
        order = input("What would you like? (espresso/latte/cappuccino):")
        if order == "off":
            return
        elif order == "report":
            print(f'Water: {self.resources["water"]}ml \nMilk: {self.resources["milk"]}ml \nCoffee: {self.resources["coffee"]}g \nMoney: ${self.money}')
            return self.turn_on()
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            print(self.process_order(order))
            return self.turn_on()


A = CoffeeMachine()
A.turn_on()


