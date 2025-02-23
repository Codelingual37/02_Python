from turtle import Turtle, Screen
import random
import colorgram

yurtle = Turtle()
screen = Screen()
yurtle.shape("turtle")
yurtle.speed(3)
yurtle.penup()
yurtle.hideturtle()
screen.colormode(255)
next_line = -200
#color_list = []
#colors = colorgram.extract("tetrahydracannabinol.jpg", 100)
colors = colorgram.extract("tetrahydracannabinol.jpg", 30)

'''for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	new_color = (r, g, b)
	color_list.append(new_color)
print(color_list)'''

#This implementation still works, but for the sake of the project, the above removes the "r=/g=/b=" from extract list
#for color in colors:
#	color_list.append(color.rgb)

color_list = [(239, 238, 236), (241, 238, 240), (231, 233, 237), (230, 235, 232), (211, 155, 101), (40, 99, 129), 
(18, 47, 77), (156, 77, 58), (147, 58, 76), (117, 37, 53), (124, 164, 183), (130, 171, 151), (41, 125, 96), 
(11, 96, 61), (73, 34, 44), (217, 199, 133), (209, 91, 66), (193, 86, 104), (192, 133, 149), (17, 59, 48), 
(168, 153, 60), (40, 58, 106), (50, 153, 186), (36, 169, 129), (169, 204, 195), (10, 88, 108), (52, 45, 42), 
(81, 80, 35), (116, 113, 156), (103, 41, 37)]

for i in range(10):
	yurtle.setx(-250)
	yurtle.sety(next_line)
	yurtle.dot(20, random.choice(color_list))
	for i in range(9):
		yurtle.forward(50)
		yurtle.dot(20, random.choice(color_list))
	next_line += 50

screen.mainloop()