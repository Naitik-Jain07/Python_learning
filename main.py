from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
## Use screen.tracer(n, delay) to manage animation speed: n=0 disables auto updates (requires screen.update()), higher n speeds up drawing

r_paddle = Paddle((350 ,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce()

    # detection of collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor()>340 or ball.distance(l_paddle) < 50 and ball.xcor()<-340:
        ball.rebound_x()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()