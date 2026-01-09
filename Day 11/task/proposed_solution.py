import random
from art import logo
# hint 4 - create a deal_card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    # return a random card from deck
    return card

# Hint 6 -> Create a function called calculate_score()
# that takes a List of cards as input and returns the sum of all the cards in the List as the score.
# Google the sum() function to help you do this.
def calculate_score_v1(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    return sum(cards)

# Hint 7
# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
# and return 0 instead of the actual score.
# 0 will represent a blackjack in our game.
def calculate_score(draw_cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(draw_cards) == 21 and len(draw_cards) == 2:
        return 0
    # check one ace at time if it is convent change the value
    while 11 in draw_cards and sum(draw_cards) > 21:
        draw_cards.remove(11)
        draw_cards.append(1)
    return sum(draw_cards)

# Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win"
    elif u_score > 21:
        return "You went over. You lose"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_blackjack_game():
    print(f"{logo}")
    # Hint 5 -> Deal the user and computer 2 cards each using deal_card() and append().
    # initialize player cards and dealer cards
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    #draw the player cards - 2 times
    #draw dealer cards - remember only one is shown
    # range started from 0 -> until 2 elements!!!!
    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 11: The score will need to be rechecked with every new card drawn
    # and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        # Hint 9: Call the function calculate_score().
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # logs to check
        print(f"Your cards : {user_cards}, your score {user_score}")
        # print(f"Computer cards: {computer_cards}, the computer's score {computer_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # Hint 10:If the game has not ended, ask the user if they want to draw another card.
        # If yes, then use the deal_card() function to add another card to the user_cards List.
        # If no, then the game has ended.
        else:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_game == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Computer final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n"*20)
    play_blackjack_game()