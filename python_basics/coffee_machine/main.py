from data import MENU, resources
from art import logo

Penny = 0.01
Nickel = 0.05
Dime = 0.1
Quarter = 0.25

def clear_screen():
    print("\n" * 20)

def calculate_coin():
    Amount_Penny = int(input("How many Penny: "))
    Amount_Nickel = int(input("How many Nickel: "))
    Amount_Dime = int(input("How many Dime: "))
    Amount_Quarter = int(input("How many quarters: "))
    Total_amount = (Penny*Amount_Penny + Nickel*Amount_Nickel + Dime*Amount_Dime + Quarter*Amount_Quarter)
    return round(Total_amount, 2)

def successful_transaction_resource(user_input, resources, MENU):
    ingredients = MENU[user_input]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            return False
    return True

def enough_money(user_input, user_money):
    price = MENU[user_input]["cost"]
    if user_money >= price:
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def process_transaction(resources, user_input):
    for item in MENU[user_input]["ingredients"]:
        if item in resources:
            resources[item] -= MENU[user_input]["ingredients"][item]
    resources["money"] += MENU[user_input]["cost"]

def report_missing_ingredient(user_input):
    print("Sorry, we cannot make your drink due to the following:")
    for item in MENU[user_input]["ingredients"]:
        if resources[item] < MENU[user_input]["ingredients"][item]:
            print(f" - Not enough {item}. Need {MENU[user_input]['ingredients'][item] - resources[item]} more.")
    print("-" * 40)

def main():
    print(logo)
    off_button = False
    while not off_button:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == 'report':
            for key, value in resources.items():
                if key == "money":
                    print(f"{key}: ${value}")
                else:
                    print(f"{key}: {value}ml")
        elif user_input in MENU:
            if successful_transaction_resource(user_input, resources, MENU):
                user_money = calculate_coin()
                if enough_money(user_input, user_money):
                    change = user_money - MENU[user_input]["cost"]
                    print(f"You have just put ${round(user_money, 2)}")
                    print(f"Here is the change: ${round(change, 2)}")
                    process_transaction(resources, user_input)
                    print("Enjoy your drink!")
                    clear_screen()
                else:
                    print("Sorry, not enough money.")
                    clear_screen()
            else:
                report_missing_ingredient(user_input)
                clear_screen()
        elif user_input == 'off':
            off_button = True
        else:
            print("Invalid input. Please choose a valid option: espresso, latte, cappuccino, report, or off.")
            clear_screen()

main()
