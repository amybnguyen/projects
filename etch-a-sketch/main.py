from turtle import Turtle, Screen

screen = Screen()
toto = Turtle()
def move_forward():
    toto.forward(10)


def move_backward():
    toto.backward(10)


def rotate_counterclockwise():
    current = toto.heading()
    toto.setheading(current + 10)


def rotate_clockwise():
    current = toto.heading()
    toto.setheading(current - 10)


def clear():
    toto.clear()
    toto.penup()
    toto.home()
    toto.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()