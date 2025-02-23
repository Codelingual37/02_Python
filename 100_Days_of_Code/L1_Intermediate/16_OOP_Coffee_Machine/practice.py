'''from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("BlueViolet")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
#my_screen.mainloop()
my_screen.exitonclick()'''

from prettytable import PrettyTable
table = PrettyTable()
names = ["Pikachu", "Squirtle", "Charmander"]
type = ["Electric", "Water", "Fire"]
table.add_column("Pokemon Name", names)
table.add_column("Type", type)
table.align = "l"
print(table)