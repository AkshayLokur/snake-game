from turtle import Turtle


class Snake:

    def __init__(self, snake_body_length):
        self.snake_body_length = snake_body_length
        self.make_snake()

    def make_snake(self):
        x_pos = 0
        for i in range(0, self.snake_body_length):
            t = Turtle(shape="square")
            t.color("white")
            t.goto(x_pos, y=0)
            x_pos -= 20
