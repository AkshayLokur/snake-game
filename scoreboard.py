from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 275)

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.color("white")
        print(f"Score is: {self.score}")
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 16, 'normal'))
