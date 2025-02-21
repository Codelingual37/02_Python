from turtle import Turtle, Screen

yurtle = Turtle()
screen = Screen()

for i in range(15):
	yurtle.forward(10)
	yurtle.penup()
	yurtle.forward(10)
	yurtle.pendown()

screen.mainloop()