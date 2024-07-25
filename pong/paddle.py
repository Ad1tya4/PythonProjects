from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcoor, ycoor):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.goto(xcoor, ycoor)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)



    def up(self):
        self.goto(self.xcor(),self.ycor()+30)
    def down(self):
        self.goto(self.xcor(),self.ycor()-30)
#     self.forward(10)
