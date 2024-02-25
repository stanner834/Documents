from main import MENU

class CoffeeMachine: #instance attributes
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0
        }
#self is used to access methods of the class, or access attributes associated when the class is instantiated
    def check_resources(self, drink):
        for ingredient, amount in drink['ingredients'].items():
            if self.resources[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self, cost):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.1
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total_money = quarters + dimes + nickels + pennies
        if total_money < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif total_money > cost:
            change = round(total_money - cost, 2)
            print(f"Here is ${change} in change.")
        self.resources['money'] += cost
        return True

    def make_coffee(self, drink,choice):
        for ingredient, amount in drink['ingredients'].items():
            self.resources[ingredient] -= amount
        print(f"Here is your {choice}. Enjoy!")

    def serve(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == 'off':
                print("Turning off the coffee machine.")
                break
            elif choice == 'report':
                self.print_report()
            else:
                drink = MENU.get(choice)
                if drink:
                    if self.check_resources(drink):
                        if self.process_coins(drink['cost']):
                            self.make_coffee(drink,choice)
                    else:
                        continue
                else:
                    print("Invalid choice. Please try again.")

    def print_report(self):
        for item, quantity in self.resources.items():
            if item != 'money':
                print(f"{item.capitalize()}: {quantity}ml" if item != 'coffee' else f"{item.capitalize()}: {quantity}g")
            else:
                print(f"{item.capitalize()}: ${quantity}")

machine = CoffeeMachine()
machine.serve()


