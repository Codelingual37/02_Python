from turtle import Turtle

MOVE_DISTANCE = 20
LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):
		self.snake = []
		self.length = LENGTH
		self.x_cor = 0
		self.y_cor = 0
		self.initialized = False
		self.create_snake()
		self.head = self.snake[0]

	def create_snake(self):
		for seg in range(self.length):
			self.grow_snake(seg)
		self.initialized = True

	def grow_snake(self, position):
		seg = Turtle(shape="square")
		seg.color("white")
		seg.penup()
		if not self.initialized:
			seg.goto(x=self.x_cor, y=self.y_cor)
			self.x_cor -= 20
		elif self.initialized:
			seg.goto(position)
		self.snake.append(seg)
	
	def extend(self):
		self.grow_snake(self.snake[-1].position())

	def reset(self):
		for seg in self.snake:
			seg.goto(1000, 1000)
		self.snake.clear()
		self.initialized = False
		self.create_snake()
		self.head = self.snake[0]

	def move(self):
		for seg in range(len(self.snake) - 1, 0, -1):
			last_x = self.snake[seg - 1].xcor()
			last_y = self.snake[seg - 1].ycor()
			self.snake[seg].goto(last_x, last_y)
		self.head.forward(MOVE_DISTANCE)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)
