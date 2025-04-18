import time
import random
from turtle import Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard 

screen = Screen() 
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    if random.randint(1,6) ==1:
        car.create_car()
    
    car.moving_cars()

    for each_car in car.car_list:
        if turtle.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.finish_line():
        car.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
