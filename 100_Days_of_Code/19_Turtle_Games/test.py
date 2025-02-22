from turtle import Turtle
import random

a_aron = Turtle()
tim_othy = Turtle()
b_lake = Turtle()
jac_queline = Turtle()
de_nise = Turtle()
o_shaug_hnessy = Turtle()
competitors = [a_aron, tim_othy, b_lake, jac_queline, de_nise, o_shaug_hnessy]

a_aron.shape("turtle")
a_aron.color("red")
#a_aron.penup()
#a_aron.goto(x=-230, y=-150)

tim_othy.shape("turtle")
tim_othy.color("orange")
#tim_othy.penup()
#tim_othy.goto(x=-230, y=-100)

b_lake.shape("turtle")
b_lake.color("yellow")
#b_lake.penup()
#b_lake.goto(x=-230, y=-50)

jac_queline.shape("turtle")
jac_queline.color("green")
#jac_queline.penup()
#jac_queline.goto(x=-230, y=0)

de_nise.shape("turtle")
de_nise.color("blue")
#de_nise.penup()
#de_nise.goto(x=-230, y=50)

o_shaug_hnessy.shape("turtle")
o_shaug_hnessy.color("purple")
#o_shaug_hnessy.penup()
#o_shaug_hnessy.goto(x=-230, y=100)

print(a_aron.color)
current = random.choice(competitors)
print(current.color)