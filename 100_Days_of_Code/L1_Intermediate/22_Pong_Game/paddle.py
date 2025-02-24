from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.speed("fastest")
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.goto(position)
		self.setheading(90)

	def move_player_up(self):
		self.forward(MOVE_DISTANCE)

	def move_player_down(self):
		self.backward(MOVE_DISTANCE)
