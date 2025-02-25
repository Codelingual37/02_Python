from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
	def __init__(self):
		self.cars = []
		self.speed = 0
		self.create_car()
		self.drive()
		
	def create_car(self):
		random_chance = random.randint(1, 6)
		if random_chance == 1:
			car = Turtle("square")
			car.hideturtle()
			car.shapesize(stretch_wid=1, stretch_len=2)
			car.setheading(180)
			car.color(random.choice(COLORS))
			car.penup()
			car.goto(300, random.randint(-250, 250))
			self.cars.append(car)
		self.drive()
	
	def drive(self):
		for car in self.cars:
			car.forward(STARTING_MOVE_DISTANCE + (self.speed * MOVE_INCREMENT))
			if -340 < car.xcor() < 300:
				car.showturtle()
			if car.xcor() < -340:
				car.hideturtle()
				car.goto(300, random.randint(-250, 250))
				
	def increase_car_speed(self):
		self.speed += 1