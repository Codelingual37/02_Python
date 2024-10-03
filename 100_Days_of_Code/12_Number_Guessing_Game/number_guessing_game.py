from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == 'easy':
    guesses = 10
else:
    guesses = 5

global PLAYER_GUESS

while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    PLAYER_GUESS = int(input("Make a guess: "))
    if PLAYER_GUESS < number:
        print("Too low.")
        print("Guess again.")
    elif PLAYER_GUESS > number:
        print("Too high.")
        print("Guess again.")
    elif PLAYER_GUESS == number:
        break
    guesses -= 1
if guesses == 0 and PLAYER_GUESS != number:
    print("You've run out of guesses. You lose!")
elif PLAYER_GUESS == number:
    print(f"You got it! The answer was {number}.")