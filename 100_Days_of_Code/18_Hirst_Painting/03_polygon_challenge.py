from turtle import Turtle, Screen
import random

yurtle = Turtle()
screen = Screen()
colors = ["AliceBlue", "BlueViolet", "Cyan2", "DarkGreen", "DarkOliveGreen1", "IndianRed", "firebrick1", "peru", 
"red1", "VioletRed", "wheat1", "MistyRose3", "DarkSlateGray", "DarkSlateBlue", "chartreuse2"]

def draw_shape(sides):
	for i in range(sides):
		yurtle.forward(50)
		yurtle.right(360/sides)

for number in range(3, 11):
	yurtle.color(random.choice(colors))
	draw_shape(number)

screen.mainloop()