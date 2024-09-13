import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock, Paper, Scissors!!! LFG.")
choices = ["rock", "paper", "scissors"]
player = input("Which one do you choose? ").lower()
win = ["Winner, winner, chicken dinner.", "Ain't nobody top ya, bruh!", "You are the enlightened one.",
       "All you do is win, win, win, no matter what.", "Started from the bottom, now you here.", "You win!"]
lose = ["You lose.", "Better luck next time.", "It's just not your day.", "Yeah, you thought...",
        "We all fail sometimes", "Maybe guess better next time."]
computer = random.choice(choices)

if player == "rock":
    print("Player: Rock")
    print(rock)
    if computer == "rock":
        print("Computer: Rock")
        print(rock)
        print("It's a draw!")
    elif computer == "paper":
        print("Computer: Paper")
        print(paper)
        print(random.choice(lose))
    else:
        print("Computer: Scissors")
        print(scissors)
        print(random.choice(win))
elif player == "paper":
    print("Player: Paper")
    print(paper)
    if computer == "paper":
        print("Computer: Paper")
        print(paper)
        print("It's a draw!")
    elif computer == "scissors":
        print("Computer: Scissors")
        print(scissors)
        print(random.choice(lose))
    else:
        print("Computer: Rock")
        print(rock)
        print(random.choice(win))
elif player == "scissors":
    print("Player: Scissors")
    print(scissors)
    if computer == "scissors":
        print("Computer: Scissors")
        print(scissors)
        print("It's a draw!")
    elif computer == "rock":
        print("Computer: Rock")
        print(rock)
        print(random.choice(lose))
    else:
        print("Computer: Paper")
        print(paper)
        print(random.choice(win))
else:
    print("You can only pick one of the three choices")