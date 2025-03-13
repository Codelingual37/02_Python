from turtle import Turtle

class StateName(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.speed("fastest")