import turtle
import pandas
from write import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_read = pandas.read_csv("50_states.csv")
states_list = states_read.state.to_list()
state_name = StateName()
guess_list = []

while len(guess_list) < 50:
	answer = screen.textinput(title=f"{len(guess_list)}/50 States Correct", prompt="What's another state's name? ").title()
	if answer == "Exit":
		missed = []
		for state in states_list:
			if state not in guess_list:
				missed.append(state)
		new_data = pandas.DataFrame(missed)
		new_data.to_csv("states_to_learn.csv")
		screen.bye()
		break
	if answer in guess_list:
		continue
	if answer in states_list:
		guess_list.append(answer)
		state = states_read[states_read.state == answer]
		state_name.goto(state.x.item(), state.y.item())
		state_name.write(answer, align="center", font=("Courier", 6, "normal"))

screen.mainloop()