from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for num in range(3):
            x_pos = 0 - 20 * num
            self.add_segment((x_pos, 0))

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.body.append(t)

    def extend(self):
        self.add_segment(self.body[-1].pos())

    def move_snake(self):
        for seg in range(len(self.body) - 1, 0, -1):
            self.body[seg].goto(self.body[seg - 1].xcor(), self.body[seg - 1].ycor())
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
