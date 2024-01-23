from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "purple", "orange", "brown"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    turtle_position = -150 + 50 * turtle_index
    new_turtle.goto(x = -230, y = turtle_position)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()