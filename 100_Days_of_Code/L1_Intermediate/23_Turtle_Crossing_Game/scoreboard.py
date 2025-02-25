from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")
LOSE_MESSAGES = ["You are done!", "You are clearly not speed.", "Better luck next time.", "Yeah, you thought..."]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        #self.color("white")   <-- Uncomment for night version
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)
    
    def game_over(self):
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 0)
        self.write(random.choice(LOSE_MESSAGES), align="center", font=FONT)
        self.speed("fastest")
        self.goto(0, -30)
        self.write("GAME OVER", align="center", font=FONT)