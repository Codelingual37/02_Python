from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Trebuchet MS", 15, "bold")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.speed("fastest")
		self.goto(x=0, y=280)
		self.score = 0
		self.high_score = 0
		self.update_score()

	def update_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score:  {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
	
	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
		self.score = 0
		self.update_score()
