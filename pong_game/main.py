from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball = Ball()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # bounce wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    # bounce paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()

    #misses
    if ball.xcor()>380:
        ball.reset()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()

screen.exitonclick()

