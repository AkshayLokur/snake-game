from turtle import Turtle

MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self, snake_body_length):
        self.body = []
        self.x_pos = 0
        self.snake_body_length = snake_body_length
        self.make()
        self.head = self.body[0]

    def make(self):
        for i in range(0, self.snake_body_length):
            t = self.__create_snake()
            self.body.append(t)

    def __create_snake(self):
        t = Turtle(shape="square")
        t.penup()
        t.goto(self.x_pos, y=0)
        t.color("white")
        self.x_pos -= 20
        return t

    def extend_length(self):
        self.body.append(self.__create_snake())

    def detect_collision_with_body(self):
        for b in self.body:
            if self.head != b and self.head.distance(b) < 15:
                return True

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
