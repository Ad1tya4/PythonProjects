from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.xmove = 3
        self.ymove = 3

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce(self):
        self.ymove  *= -1

    def reflect(self):
        self.xmove *= -1

    def reset(self, player):
        self.goto(0,0)
        self.xmove *= player
