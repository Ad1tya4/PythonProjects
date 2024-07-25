from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
game = True
screen = Screen()
ball = Ball()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
paddle = Paddle(350,0)
paddle_2 = Paddle(-350,0)
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")
while game:
    screen.update()
    ball.move()
    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce()
    if ball.xcor()> 320 and ball.distance(paddle)< 50 or ball.xcor()<-320 and ball.distance(paddle_2)<50:
        ball.reflect()
    if ball.xcor() < -400:
        ball.reset(1)
    if ball.xcor() > 400:
        ball.reset(-1)





















screen.exitonclick()
