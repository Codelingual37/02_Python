from turtle import Turtle, Screen
import random

yurtle = Turtle()
screen = Screen()
direction = [0, 90, 180, 270]

screen.colormode(255)
yurtle.pensize(20)
yurtle.speed(8)

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

for i in range(100):
	yurtle.color(random_color())
	yurtle.forward(50)
	yurtle.setheading(random.choice(direction))

screen.mainloop()