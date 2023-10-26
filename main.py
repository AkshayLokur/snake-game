from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game :)")
screen.tracer(0)  # to disable automatic screen tracing / refresh / animation

snake = Snake(snake_body_length=3)
food = Food()
scoreboard = ScoreBoard()
screen.update()

screen.listen()  # listen to keystrokes
# Bind Arrow keys
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Eat food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_length()
        scoreboard.update_scoreboard()

    # Collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    # Collision with body
    if snake.detect_collision_with_body():
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()
