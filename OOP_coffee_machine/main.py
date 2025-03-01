from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine() 
coffee_machine = CoffeeMaker() 

off_button = False
while not off_button:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}: ").lower()

    if user_input == "report":
        money_machine.report()
        coffee_machine.report()
    elif user_input == "off":
        print("turning off...")
        off_button = True
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_machine.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)


