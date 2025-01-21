import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
# tim.penup()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    new_heading = tim.heading()+ 10
    tim.setheading(new_heading)
    tim.forward(10)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun=move_forward)
screen.onkey(key = "a", fun=move_left)
screen.onkey(key = "s", fun=move_backward)
screen.onkey(key = "d", fun=move_right)
screen.onkey(key = "c", fun=clear_screen)
screen.exitonclick()
