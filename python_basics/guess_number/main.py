import random
from art import logo
# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def generate_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)


def play_game(target_number, attempts):
    """Main game logic: User guesses the number within the given attempts."""
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess > target_number:
            print("Too high.")
        elif guess < target_number:
            print("Too low.")
        else:
            print(f"Congratulations! You guessed the number {target_number}.")
            return
        attempts -= 1

    print(f"You've run out of guesses. The correct number was {target_number}.")


def choose_difficulty():
    """Prompts the user to choose a difficulty level."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy':
            return EASY_LEVEL_TURNS
        elif level == 'hard':
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")


def main():
    """Main entry point for the number guessing game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    target_number = generate_number()
    attempts = choose_difficulty()
    play_game(target_number, attempts)


if __name__ == "__main__":
    main()
