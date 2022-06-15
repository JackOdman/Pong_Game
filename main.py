from turtle import Turtle, Screen
from pongs import PongOne
import ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.tracer(0)

pong_one = PongOne((270, 0))
pong_two = PongOne((-270, 0))
ball = ball.Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pong_one.up, "Up")
screen.onkey(pong_one.down, "Down")
screen.onkey(pong_two.up, "w")
screen.onkey(pong_two.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.motion()

    #Detect collision with wall
    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(pong_one) < 50 and ball.xcor() > 250 or ball.distance(pong_two) < 50 and ball.xcor() < -250:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()