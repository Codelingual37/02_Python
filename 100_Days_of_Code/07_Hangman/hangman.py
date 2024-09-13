import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6
chosen_word = random.choice(word_list)
print(logo)

word_length = len(chosen_word)
placeholder = "_" * word_length
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}. Guess another letter.")

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

    if guess not in chosen_word:
        print(f"You guessed {guess}, which isn't in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"The correct word was {chosen_word}. YOU LOSE!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
