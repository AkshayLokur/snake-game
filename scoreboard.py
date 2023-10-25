from turtle import Turtle


class ScoreBoard(Turtle):
    TEXT_ALIGNMENT = "center"
    FONT = ('Courier New', 16, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.goto(0, 275)
        self.color("white")

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        print(f"Score is: {self.score}")
        self.write(f"Score = {self.score}", False, align=ScoreBoard.TEXT_ALIGNMENT, font=ScoreBoard.FONT)

    def game_over(self):
        print("GAME OVER!")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ScoreBoard.TEXT_ALIGNMENT, font=ScoreBoard.FONT)
