from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the read? Enter a colour: ")


def create_turtles():
    turtles = []
    for x in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(x)
        turtles.append(turtle)
    return turtles


def start_race(turtles):
    height = -100
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=-220, y=height)
        height += 40


def get_winner(turtles):
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(10, 20))
            if turtle.xcor() > 200:
                return turtle.color()[0]


turtles = create_turtles()
start_race(turtles)
winner = get_winner(turtles)
if winner == bet.lower():
    print(f"Congratuations, {winner} won! You guessed correctly")
else:
    print(f"Unlucky, {winner} won! You loose!")

screen.exitonclick()


