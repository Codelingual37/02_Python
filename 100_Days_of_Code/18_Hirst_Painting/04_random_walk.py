from turtle import Turtle, Screen
import random

yurtle = Turtle()
screen = Screen()
colors = ["AliceBlue", "BlueViolet", "Cyan2", "DarkGreen", "DarkOliveGreen1", "IndianRed", "firebrick1", "peru", 
"red1", "VioletRed", "wheat1", "MistyRose3", "DarkSlateGray", "DarkSlateBlue", "chartreuse2"]
direction = [0, 90, 180, 270]

yurtle.pensize(20)
yurtle.speed(8)


for i in range(100):
	yurtle.color(random.choice(colors))
	yurtle.forward(50)
	yurtle.setheading(random.choice(direction))

screen.mainloop()
