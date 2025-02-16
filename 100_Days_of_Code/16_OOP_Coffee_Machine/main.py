from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

m_machine = MoneyMachine()
c_maker = CoffeeMaker()
drinkmenu = Menu()

while machine_on:
	coffee = input(f"What would you like ({drinkmenu.get_items()})? ").lower()
	if coffee == "off":
		machine_on = False
		break
	elif coffee == "report":
		c_maker.report()
		m_machine.report()
		continue
	drink = drinkmenu.find_drink(coffee)
	if c_maker.is_resource_sufficient(drink) and m_machine.make_payment(drink.cost):
		c_maker.make_coffee(drink)
	