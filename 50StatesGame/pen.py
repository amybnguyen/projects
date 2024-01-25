from turtle import Turtle
FONT = ("Arial", 8, "normal")
WINNING_FONT = ("Arial", 24, "normal")


class Pen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def display_state(self, state, x, y):
        self.goto(x,y)
        self.write(f"{state}", align="center", font=FONT)

    def win(self):
        self.goto(0,0)
        self.write(f"YOU WIN!", align="center", font=WINNING_FONT)