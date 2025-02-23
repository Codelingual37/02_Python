from art import logo, vs
from game_data import data
import random

print(logo)

game = 'y'
score = 0
data_len = len(data)
vowels = "aeiou"


def article(description):
    if description[0].lower() in vowels:
        return "an"
    else:
        return "a"


while game == 'y':
    first = 'y'
    if first == 'y':
        choice_a = data[random.randint(0, data_len)]
        data.pop(data.index(choice_a))
        data_len -= 1
        choice_b = data[random.randint(0, data_len)]
    first = 'n'
    print(f"Compare A: {choice_a["name"]}, {article(choice_a["description"])} {choice_a["description"]} from {choice_a["country"]}")
    print(vs)
    print(f"Against B: {choice_b["name"]}, {article(choice_b["description"])} {choice_b["description"]} from {choice_b["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
        choice = choice_a
        compare = choice_b
    else:
        choice = choice_b
        compare = choice_a
    if choice["follower_count"] > compare["follower_count"]:
        score += 1
        if compare in data:
            data.pop(data.index(compare))
            data_len -= 1
        choice_a = choice
        if choice in data:
            data.pop(data.index(choice))
            data_len -= 1
        choice_b = data[random.randint(0, data_len)]
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = 'n'

