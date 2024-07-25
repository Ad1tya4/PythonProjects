import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!!!")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_on = False
        score.gameover()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10 and snake.head.distance(seg) != 0 :
            print(snake.head.distance(seg))
            print(f"current {seg}")
            print(snake.head)
            game_on = False
            score.gameover()


screen.exitonclick()
