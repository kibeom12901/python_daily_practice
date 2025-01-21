import random
from art import logo, vs
from game_data import data


def check_answer(value_1, value_2, choice):
    print("\n"*20)
    if choice == 'A' and value_1['follower_count'] > value_2['follower_count']:
        return True
    else:
        return False

def game():
    current_score = 0
    game_over = False
    A_data = random.choice(data)
    print(logo)

    while not game_over:
        print("Compare A: " + A_data['name']+ A_data['description'] + ", from " + A_data['country'])
        print(vs)
        B_data = random.choice(data)
        print("Compare B: " + B_data['name']+ B_data['description'] + ", from " + B_data['country'])
        # check_answer(A_data, B_data, current_score, game_over)

        choice = input(("Who has more followers? Type 'A' or 'B':"))

        if check_answer(A_data, B_data, choice):
            current_score += 1
            print(logo)
            print(f"You're right! Current score: {current_score}")
            A_data = B_data
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True

game()



