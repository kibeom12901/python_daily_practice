import random
from art import logo 

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    score = sum(cards)
    while 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = sum(cards)

    return score


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif u_score == 0:
        return ("Win with a Blackjack 😎")
    elif c_score == 0:
        return("Lose, opponent has Blackjack 😱")
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    for i in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    print(f"    Your cards: {user_card}, current score: {calculate_score(user_card)}")
    print(f"    Computer's first card: {computer_card[0]}")

    if calculate_score(user_card) == 0 or calculate_score(computer_card) == 0:
        game_over = True

    while not game_over:
        replay = input("Type 'y' to get another card, type 'n' to pass: ")

        if replay == 'y':
            user_card.append(deal_cards())

            user_score = calculate_score(user_card)
            print(f"    Your cards: {user_card}, current score: {user_score}")
            print(f"    Computer's first card: {computer_card[0]}")

            if user_score > 21:
                game_over = True

        elif replay == 'n':
            while sum(computer_card) < 17:
                computer_card.append(deal_cards())
            print(f"   Computer's final hand: {computer_card}, final score: {calculate_score(computer_card)}")
            game_over = True

    print(compare(calculate_score(user_card), calculate_score(computer_card)))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n"*20)
    play_game()
