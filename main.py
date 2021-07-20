from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pencolor('#32c18f')
timmy.pensize(3)
timmy.speed('fastest')
for x in range(1, 36):
    timmy.pencolor(random.random(), random.random(), random.random())
    timmy.circle(100)
    timmy.right(10)



screen = Screen()
screen.exitonclick()


