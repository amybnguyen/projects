import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

toto = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(toto.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and have them move to the left of the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Reset turtle and increase level if turtle reaches top
    if toto.ycor() > 300:
        toto.return_to_bottom()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if toto.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()