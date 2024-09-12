from art import logo

print(logo)
bids = {}
active_bidding = True
highest_bid = 0
highest_bidder = ""

while active_bidding:
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'" ).lower()
    if more_bidders == 'yes':
        print('\n' * 20)
    else:
        for key in bids:
            if highest_bid < bids[key]:
                highest_bid = bids[key]
                highest_bidder = key
        print(f'''The winner is {highest_bidder} with a bid of ${highest_bid}. 
        Congratulations {highest_bidder}!''')
        active_bidding = False
