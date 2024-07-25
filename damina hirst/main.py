# import colorgram
# colors = colorgram.extract("dhirst.jpeg",30)
# list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     list.append(new_color)
# print(list)
import turtle as t
import random

t.colormode(255)
list = [(223, 177, 3), (2, 135, 196), (7, 149, 97), (228, 114, 156), (127, 160, 203), (242, 122, 43), (26, 17, 62),
        (240, 164, 195), (232, 82, 112), (64, 12, 68), (235, 201, 46), (3, 173, 118), (83, 30, 20), (194, 15, 39),
        (231, 53, 30), (195, 69, 36), (140, 208, 236), (197, 30, 50), (6, 66, 158), (0, 123, 72), (18, 157, 206),
        (126, 181, 157), (150, 28, 21), (238, 202, 7), (180, 181, 220), (162, 209, 188)]
tim = t.Turtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed(20)


def draw():

    for _ in range(10):
        tim.dot(20, random.choice(list))
        tim.forward(50)

draw()
for _ in range(4):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50)
    draw()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.forward(50)
    draw()

tim.setheading(90)
tim.forward(50)
tim.setheading(180)
tim.forward(50)
draw()
screen = t.Screen()
screen.exitonclick()
