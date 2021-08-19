from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")


class Scoreboard(Turtle):
    def __init__(self, y=240):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, y)

        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.l_score}\t{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.display_score()

    def r_point(self):
        self.r_score += 1
        self.display_score()
