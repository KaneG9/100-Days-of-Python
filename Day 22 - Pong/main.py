import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


def score_goal(player):
    if player == 1:
        scoreboard.player_1_score += 1
    else:
        scoreboard.player_2_score += 1
    scoreboard.update_scoreboard()
    ball.reset_position()
    screen.update()
    time.sleep(2)


def play_game():
    while True:
        time.sleep(0.05)
        ball.move_ball()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.wall_bounce()
        # detect paddle collision
        if (ball.xcor() >= 320 and ball.distance(player_1) < 50) or (ball.xcor() <= -320 and ball.distance(player_2) < 50):
            ball.paddle_bounce()
        if ball.xcor() < -400:
            score_goal(1)
        elif ball.xcor() > 400:
            score_goal(2)
        screen.update()


player_1 = Paddle(1)
player_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player_1.up)
screen.onkey(key="w", fun=player_2.up)
screen.onkey(key="Down", fun=player_1.down)
screen.onkey(key="s", fun=player_2.down)
play_game()
screen.exitonclick()

