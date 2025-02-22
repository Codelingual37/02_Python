from turtle import Turtle, Screen
import random

race = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cor = [-150, -100, -50, 0, 50, 100]
competitors = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

for turtles in range(6):
	comp = Turtle(shape="turtle")
	comp.color(colors[turtles])
	comp.penup()
	comp.goto(x=-230, y=y_cor[turtles])
	competitors.append(comp)

while race:
	for turtle in competitors:
		turtle.speed(5)
		turtle.forward(random.randint(0, 10))
		if turtle.xcor() >= 230:
			race = False
			winner = turtle.pencolor()
			if winner == user_bet:
				print(f"You won the bet: {user_bet} has won the race!")
			else:
				print(f"Sorry. You lost the bet: {winner} has won the race.")
screen.bye()
screen.mainloop()
