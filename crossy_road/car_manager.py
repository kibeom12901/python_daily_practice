import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_list = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_len=1,stretch_wid=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(0)
        new_car.goto(300, random.randint(-250,250))
        self.car_list.append(new_car)


    def moving_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



    
