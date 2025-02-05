from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle() 

screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgpic(image)
guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title = f"{len(guessed_states)}/50 states correct", prompt="Whats Your Guess").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()

    if user_guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break

    if user_guess in all_states:
        guessed_states.append(user_guess)
        turtle.hideturtle()
        turtle.penup()
        state_data = data[data["state"] == user_guess]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(user_guess)

screen.mainloop()


