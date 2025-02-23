from turtle import Turtle, Screen

a_aron = Turtle()
screen = Screen()

def move_forward():
	a_aron.forward(10)
def move_backward():
	a_aron.backward(10)
def turn_left():
	a_aron.left(10)
def turn_right():
	a_aron.right(10)
def	clear():
	a_aron.clear()
	a_aron.penup()
	a_aron.home()
	a_aron.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.mainloop()
