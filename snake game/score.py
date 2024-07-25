from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()

    def updatescore(self):
        self.write(f"Score : {self.score}", align= "center", font = ("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!", align= "center", font = ("Arial", 40, "normal"))
    def increase(self):
        self.clear()
        self.score += 1
        self.updatescore()
