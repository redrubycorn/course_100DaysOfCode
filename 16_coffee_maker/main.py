from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# prompt the user by asking what he/she likes
# check the user's input to decide what to do next
# promt should show every time action has completed, e.g. once drink dispensed
while True:
    user_input = input(f"What would you like? ({menu.get_items()}) ")
    if user_input == "report":
        # print report
        coffee_maker.report()
    elif user_input == "off":
        # turn off the coffee machine by entering off to the prompt
        print("Turn machine off")
        break
    else:
        # if items exists make coffe
        choice = menu.find_drink(user_input)
        if choice == None: # item doesn't exist so get back to prompt
            pass
        else: # continue making coffee and check if resource are sufficient
            if coffee_maker.is_resource_sufficient(choice):
                cost = choice.cost # get the cost of the item
                if money_machine.make_payment(cost): # process coins and make payment
                    coffee_maker.make_coffee(choice) # make the coffe