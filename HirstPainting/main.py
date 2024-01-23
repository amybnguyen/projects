# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

toto = Turtle()
toto.speed(0)

rgb_colors = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
toto.penup()
toto.hideturtle()
toto.setheading(225)
toto.forward(300)
toto.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    toto.dot(20, random.choice(rgb_colors))
    toto.forward(40)
    if dot_count % 10 == 0:
        toto.setheading(90)
        toto.forward(40)
        toto.setheading(180)
        toto.forward(400)
        toto.left(180)


screen.exitonclick()