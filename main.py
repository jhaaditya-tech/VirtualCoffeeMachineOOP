#Object Oriented Programming Language
import menu
import coffee_maker
import money_machine

money_machine=money_machine.MoneyMachine()
available_resources=coffee_maker.CoffeeMaker()
menu=menu.Menu()

is_on=True

while is_on:
    options=menu.get_items()
    user_input=input(f"Please choose your flavor: {options}: \t")
    if user_input=="off":
        is_on=False
    elif user_input=="report":
        money_machine.report()
        available_resources.report()
    else:
        drink=menu.find_drink(user_input)
        if available_resources.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                available_resources.make_coffee(drink)










