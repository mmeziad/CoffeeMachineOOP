from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()
# m_item = MenuItem()

while True:
    userIn = input("What would you like? (espresso/latte/cappuccino): ")
    print(userIn)
    if userIn == "off":
        break
    elif userIn == "report":
        maker.report()
    elif menu.find_drink(userIn) is not None:
        item = menu.find_drink(userIn)
        if maker.is_resource_sufficient(item) is True:
            # coins_inserted = machine.process_coins()
            if machine.make_payment(item.cost) is True:
                machine.report()
                maker.make_coffee(item)






