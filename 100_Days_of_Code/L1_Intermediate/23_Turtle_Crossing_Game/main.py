import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

#uncomment for night version
#night_version = screen.bgcolor("black")
#player.color("white")

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    if player.crossed_finish_line():
        score.increase_score()
        player.return_to_start()
        cars.increase_car_speed()
    for car in cars.cars:
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()

screen.mainloop()