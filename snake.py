from turtle import Turtle

MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self, snake_body_length):
        self.body = []
        self.snake_body_length = snake_body_length
        self.make()
        self.head = self.body[0]

    def make(self):
        x_pos = 0
        for i in range(0, self.snake_body_length):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(x_pos, y=0)
            x_pos -= 20
            self.body.append(t)

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            print("moving up")
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            print("moving down")
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            print("moving left")
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            print("moving right")
            self.head.setheading(0)
