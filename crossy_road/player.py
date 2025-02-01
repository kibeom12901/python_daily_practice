from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.car_manager = CarManager

    def go_up(self):
        new_y = self.ycor()+10
        self.goto(self.xcor(),new_y)

    def finish_line(self):
        if self.ycor()>= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

            


        
