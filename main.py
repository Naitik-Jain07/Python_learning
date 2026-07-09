import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player)<20:
            game_is_on = False

    if player.is_at_finish_line():
        player.back_to_starting_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()

