from turtle import Turtle, Screen
import random

colors = ["AliceBlue", "BlueViolet", "Cyan2", "DarkGreen", "DarkOliveGreen1", "IndianRed", "firebrick1", "peru", 
"red1", "VioletRed", "wheat1", "MistyRose3", "DarkSlateGray", "DarkSlateBlue", "chartreuse2"]

travis = Turtle()
travis.shape("turtle")
travis.speed(3)
next_line = -300
for i in range(10):
	travis.teleport(-300, next_line)
	travis.dot(20, random.choice(colors))
	for i in range(9):
		travis.penup()
		travis.forward(65)
		travis.dot(20, random.choice(colors))
	next_line += 65
travis.hideturtle()

screen = Screen()
screen.mainloop()