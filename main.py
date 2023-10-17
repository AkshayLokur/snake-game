from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game :)")

snake = Snake(snake_body_length=3)

screen.exitonclick()
