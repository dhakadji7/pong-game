from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
r_score=Scoreboard((80,260))
l_score=Scoreboard((-80,260))
ball = Ball()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_onn=True
while game_is_onn:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detecting ball and wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.ball_bounce()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.paddle_bounce()

    if ball.xcor()>380:
        l_score.update_score()
        ball.reset_ball()
    if ball.xcor()<-380:
        r_score.update_score()
        ball.reset_ball()
    if l_score.score==5 or r_score.score==5:
        r_score.game_over()
        game_is_onn=False


screen.exitonclick()