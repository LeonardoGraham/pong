from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position, shape="square", screen_height=600):
        super().__init__(shape)

        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

        self.screen_height = screen_height

    def up(self):
        if self.ycor() < ((self.screen_height / 2) - 55):
            new_y = self.ycor() + SPEED
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > ((self.screen_height / -2) + 60):
            new_y = self.ycor() - SPEED
            self.goto(self.xcor(), new_y)
