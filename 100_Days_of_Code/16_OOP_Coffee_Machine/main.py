from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_state = "on"

m_machine = MoneyMachine()
c_maker = CoffeeMaker()
drinkmenu = Menu()

while machine_state == "on":
	coffee = input("What would you like? ").lower()
	if coffee == "off":
		machine_state = "off"
		break
	elif coffee == "report":
		c_maker.report()
		m_machine.report()
		continue
	drink = drinkmenu.find_drink(coffee)
	if drink == None:
		print(f"Please choose one of the following: {drinkmenu.get_items()}")
		continue
	if not c_maker.is_resource_sufficient(drink):
		continue
	if not m_machine.make_payment(drink.cost):
		continue
	c_maker.make_coffee(drink)
	