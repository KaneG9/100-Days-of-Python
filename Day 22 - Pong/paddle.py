from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.color("white")
        self.player = player
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(UP)
        self.set_position()

    def set_position(self):
        if self.player == 1:
            self.goto(350, 0)
        else:
            self.goto(-350, 0)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)