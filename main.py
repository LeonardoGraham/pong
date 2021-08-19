from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(position=(-350, 0), screen_height=SCREEN_HEIGHT)
r_paddle = Paddle(position=(350, 0), screen_height=SCREEN_HEIGHT)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

l_score = 0
r_score = 0

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)

    ball.move()

    if ball.ycor() >= (SCREEN_HEIGHT / 2) - 10 or (ball.ycor() <= (SCREEN_HEIGHT / -2) + 20):
        ball.bounce_y()
    if ball.xcor() == l_paddle.xcor() + 20 and (
            l_paddle.ycor() + 50 >= ball.ycor() >= l_paddle.ycor() - 50) or ball.xcor() == r_paddle.xcor() - 20 and (
            r_paddle.ycor() + 50 >= ball.ycor() >= r_paddle.ycor() - 50):
        ball.bounce_x()
    if ball.xcor() >= (SCREEN_WIDTH / 2) - 10:
        score.l_point()
        ball.reset_position()

    if ball.xcor() <= (SCREEN_WIDTH / -2):
        score.r_point()
        ball.reset_position()

screen.exitonclick()
