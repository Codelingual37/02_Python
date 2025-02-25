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
		self.update_score()

	def update_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score:  {self.score}", move=False, align=ALIGNMENT, font=FONT)

	def game_over(self, instance):
		if instance == 1:
			self.goto(x=0, y=0)
			self.write("You crashed into your tail.\n	GAME OVER.", move=False, align=ALIGNMENT, font=FONT)
		if instance == 2:
			self.goto(x=0, y=0)
			self.write("You crashed into a wall.\n       GAME OVER.", move=False, align=ALIGNMENT, font=FONT)