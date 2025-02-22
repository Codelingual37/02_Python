from turtle import Turtle, Screen
import random

yurtle = Turtle()
screen = Screen()
direction = [0, 90, 180, 270]

screen.colormode(255)
yurtle.speed(0)

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

def draw_spirograph(size_of_gap):
	for i in range(int(360 / size_of_gap)):
		yurtle.color(random_color())
		yurtle.circle(100)
		yurtle.setheading(yurtle.heading() + size_of_gap)

draw_spirograph(5)

screen.mainloop()
