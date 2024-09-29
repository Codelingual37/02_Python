from art import logo
import random

print(logo)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
play = True


def blackjack_check(hand):
    handlen = len(hand)
    if sum(hand) == 21 and handlen == 2:
        return "yes"
    else:
        return "no"


def ace_reduced_sum(hand):
    handlen = len(hand)
    ace_count = 0
    reduce = 0
    for card in hand:
        if card == deck[0]:
            ace_count += 1
    if ace_count > 1:
        reduce += (ace_count - 1) * 10
    if ace_count == 1 and handlen > 2 and sum(hand) > 21:
        reduce += 10
    total = sum(hand) - reduce
    return total


def win_or_bust(player_hand, computer_hand, player_score, computer_score):
    if blackjack_check(computer_hand) == "yes" or player_score > 21:
        print(f"Your final hand: [{player_hand}], final score: {player_score}")
        print(f"Computer's final hand: [{computer_hand}], final score: {computer_score}")
        if computer_score == 21:
            print("Your opponent got Blackjack.")
        elif player_score > 21:
            print("You went over.")
        print(f"You lost the game :(")
        return "ask"
    elif blackjack_check(player_hand) == "yes" or computer_score > 21:
        print(f"Your final hand: [{player_hand}], final score: {player_score}")
        print(f"Computer's final hand: [{computer_hand}], final score: {computer_score}")
        if player_score == 21:
            print("You got Blackjack!")
        elif computer_score > 21:
            print("Your opponent went over.")
        print(f"Congratulations! You won the game!!!")
        return "ask"
    else:
        return "continue"


while play:
    player_score = 0
    computer_score = 0
    player_hand = []
    computer_hand = []
    again = 'y'
    ask_play = input("Do you want to play Blackjack? Enter 'y' or 'n'. ").lower()
    if ask_play != 'y':
        play = False
        continue
    for start in range(2):
        player_hand.append(random.choice(deck))
        computer_hand.append(random.choice(deck))
    player_score = ace_reduced_sum(player_hand)
    computer_score = ace_reduced_sum(computer_hand)
    ask_or_continue = win_or_bust(player_hand, computer_hand, player_score, computer_score)
    if ask_or_continue == "ask":
        continue
    print(f"Your cards: [{player_hand}], current score: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")
    while again == 'y' and ask_or_continue == "continue":
        again = input("Type 'y' to get another card. Type 'n' to pass: ").lower()
        if again == 'y':
            player_hand.append(random.choice(deck))
            player_score = ace_reduced_sum(player_hand)
            ask_or_continue = win_or_bust(player_hand, computer_hand, player_score, computer_score)
            if ask_or_continue == "continue":
                print(f"Your cards: [{player_hand}], current score: {player_score}")
                print(f"Computer's first card: {computer_hand[0]}")
    if ask_or_continue == "ask":
        continue
    while computer_score < 17:
        computer_hand.append(random.choice(deck))
        computer_score = ace_reduced_sum(computer_hand)
        ask_or_continue = win_or_bust(player_hand, computer_hand, player_score, computer_score)
    if ask_or_continue == "ask":
        continue
    print(f"Your final hand: [{player_hand}], final score: {player_score}")
    print(f"Computer's final hand: [{computer_hand}], final score: {computer_score}")
    if player_score > computer_score:
        print("Your score was higher! You win!!!")
    elif player_score == computer_score:
        print("The scores were the same. The opponent wins. Sorry!")
    else:
        print("Your opponent's score was higher. Better luck next time!")
