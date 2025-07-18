# TODO-1: Ask the user for input
#  show the log first ..
from art import logo
print(logo)
# ask the name and bid
name = input("What is your name?: ")
bid = input("What is your bid?: $")

# TODO-2: Save data into dictionary {name: price}
# initialize the dictionary with the first bidder
bidders = {
    name: bid
}
# TODO-3: Whether if new bids need to be added
bid_continue = True
# ask if there are any other bidders
add_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
# update le variable for the while loop
if add_bidders == "no":
    bid_continue = False
elif add_bidders == "yes":
    bid_continue = True
else:
    print("You made a typo")

while bid_continue:
    # clear the screen
    print("\n" * 30)
    # ask the name and bid
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    # add the new bidder to the dictionary
    bidders[name] = bid
    # ask if there are any other bidders
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    # apply the same logic
    if add_bidders == "no":
        bid_continue = False
    elif add_bidders == "yes":
        bid_continue = True
    else:
        print("You made a typo")

 # TODO-4: Compare bids in dictionary
winner = ""
last_offer = 0
for item in bidders:
    # print(f"The offer of {item} is {bidders[item]}")
    if float(bidders[item]) > last_offer:
        last_offer = float(bidders[item])
        winner = item
print(f"The winner is {winner} with offer: ${last_offer}")




