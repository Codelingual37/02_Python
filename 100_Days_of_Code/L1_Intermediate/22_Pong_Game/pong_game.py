from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

net = Turtle()
net.hideturtle()
net.pensize(5)
net.penup()
net.color("white")
net_y = 300
net.setheading(270)
net.goto(0, net_y)
while net_y > -300:
	net.pendown()
	net.forward(30)
	net.penup()
	net.forward(30)
	net_y -= 60

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

game_on = True
screen.listen()
screen.onkey(key="w", fun=l_paddle.move_player_up)
screen.onkey(key="s", fun=l_paddle.move_player_down)
screen.onkey(key="Up", fun=r_paddle.move_player_up)
screen.onkey(key="Down", fun=r_paddle.move_player_down)

while game_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	if ball.distance(r_paddle) < 50 and ball.xcor() >= 325 or ball.distance(l_paddle) < 50 and ball.xcor() <= -325:
		ball.bounce_x()

	if ball.xcor() > 380:
		ball.reset_position()
		score.l_point()

	if ball.xcor() < -380:
		ball.reset_position()
		score.r_point()

screen.mainloop()