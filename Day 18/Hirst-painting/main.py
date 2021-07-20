import turtle

import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('hirst.jpg', 20)
color_list = []
for x in colors:
    color_list.append((x.rgb.r, x.rgb.g, x.rgb.b))

print(color_list)
t = Turtle()
t.penup()
turtle.colormode(255)

for x in range(5):
    t.pencolor(random.choice(color_list[3:]))
    t.dot(30)
    for y in range(4):
        t.pencolor(random.choice(color_list[3:]))
        t.forward(50)
        t.dot(30)

    if x % 2 == 0:
        angle = 90
    else:
        angle = 270
    t.right(angle)
    t.forward(50)
    t.right(angle)


screen = Screen()
screen.exitonclick()