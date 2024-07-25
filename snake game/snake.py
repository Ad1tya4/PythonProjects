from turtle import Turtle

POSITIONS = [(0, 0), (20, 0), (-20, 0)]
MOV_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for POS in POSITIONS:
            self.add_seg(POS)

    def move(self):
        self.head.forward(MOV_DIST)
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
    def add_seg(self, POS):
        new_turtle = Turtle()
        # new_turtle.shapesize(0.5,0.5)
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.setposition(POS)
        self.segments.append(new_turtle)


    def  extend(self):
        self.add_seg(self.segments[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
