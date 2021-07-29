from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic sans", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_center()
        self.goto(x=0, y=220)
        self.write(f"{self.player_2_score}         {self.player_1_score}", align=ALIGNMENT, font=FONT)

    def draw_center(self):
        self.goto(0, 300)
        for x in range(6):
            self.pendown()
            self.setheading(90)
            self.forward(50)
            self.penup()
            self.forward(50)
