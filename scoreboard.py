from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Level {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.add_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
