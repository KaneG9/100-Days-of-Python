from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


def play_game():
    while True:
        time.sleep(0.1)
        snake.move_snake()
        screen.update()

        # detect collision  with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            return

        # detect collision with tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                return


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
play_game()
screen.exitonclick()

