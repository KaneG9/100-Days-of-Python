from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.y_move += 1
        self.x_move += 1

    def reset_position(self):
        self.goto(0, 0)
        self.y_move = 10
        if self.x_move > 0:
            self.x_move = 10
        else:
            self.x_move = -10
        self.paddle_bounce()

