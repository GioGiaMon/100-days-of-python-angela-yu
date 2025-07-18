#  show the log first ...
from art import logo
print(logo)

# function to get the highest bid
# input dictionary name: bid
def find_highest_bid(bidders):
    # initialize histest bid and winner name
    winner = ""
    max_bid = 0
    # loop in the dictionary
    for bid in bidders:
        if bidders[bid] > max_bid:
            max_bid = bidders[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of: ${max_bid}")

# function to check if the bid is valid
def is_valid_bid():
    while True:
        bid_input = input("What is your bid?: $")
        if bid_input.replace('.','',1).isdigit():
            return float(bid_input)
        else:
            print("Please enter a valid number.")
# function to check yes or no
def check_yes_or_no(answer):
    while True:
        response = input(answer).lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Please type only 'yes' or 'no'")

# always ask for the first bidder
bid_continue = True
# initialize the bidders dictionary
bidders = {}
while bid_continue:
    # ask name and bid
    name = input("What is your name?: ")
    # Check the bid is correct
    # bid = input("What is your bid?: $")
    bid = is_valid_bid()
    # add to the dictionary
    bidders[name] = bid
    # Check if there are any other bidders
    add_bidders = check_yes_or_no("Are there any other bidders? Type 'yes' or 'no'.\n")
    if add_bidders == "yes":
        # clear the screen
        print("\n" * 20)
    elif add_bidders == "no":
        # stop the loop
        bid_continue = False
        # print the winner
        find_highest_bid(bidders)





