import random
from hangman_words import word_list
from hangman_art import stages, logo

# Initialize lives
lives = 6

# Display the logo
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # Debug: Remove in production

# Create placeholders for the word to guess
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    # Display remaining lives
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print("You've already guessed", guess)

    # Update placeholders based on the guess
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + ", that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")

    # Check if the game is won
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # Display the current stage
    print(stages[lives])
