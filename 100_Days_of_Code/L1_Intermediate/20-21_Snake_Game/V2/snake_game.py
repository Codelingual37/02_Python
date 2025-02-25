from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		score.update_score()

	for seg in snake.snake[1:]:
		if snake.head.distance(seg) < 5:
			score.reset()
			snake.reset()
	if snake.head.xcor() <= -300 or snake.head.ycor() <= -300 or snake.head.xcor() >= 300 or snake.head.ycor() >= 300:
		score.reset()
		snake.reset()

screen.mainloop()