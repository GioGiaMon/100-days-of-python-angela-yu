from art import logo
import random

play_a_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(dealer_cards):
    if sum(dealer_cards) < 17:
        dealer_cards.append(random.sample(cards, 1)[0])

def calculate_score(draw_cards):
    # check one ace at time if it is convent change the value
    while 11 in draw_cards and sum(draw_cards) > 21:
        draw_cards.remove(11)
        draw_cards.append(1)
    return sum(draw_cards)

while play_a_game == 'y':
    print(logo)
    drop_cards = random.sample(cards, 2)
    print(f"Your cards: {drop_cards}, current score {calculate_score(drop_cards)}",)
    computer_cards = random.sample(cards, 1)
    print(f"Computer's first card: {computer_cards[0]}")
    get_new_card = input("Type 'y' to get another card, type 'n' to pass:  ")
    while get_new_card == 'y' and calculate_score(drop_cards) <= 21:
        new_card = random.sample(cards, 1)[0]
        drop_cards.append(new_card)
        player_sum = calculate_score(drop_cards)
        print(f"Your cards: {drop_cards}, current score {player_sum}", )
        print(f"Computer's first card: {computer_cards[0]}")
        if player_sum > 21:
            break
        get_new_card = input("Type 'y' to get another card, type 'n' to pass:  ")
    deal_card(computer_cards)
    print(f"Your final hand: {drop_cards}, final score {calculate_score(drop_cards)}")
    print(f"Computer's final hand is {computer_cards}, final score: {calculate_score(computer_cards)}")
    if sum(drop_cards) > 21:
        print(f"You went over. You lose.")
    elif sum(drop_cards) > sum(computer_cards) and calculate_score(computer_cards) < 21:
        print(f"You win")
    elif sum(drop_cards) <=21 and calculate_score(computer_cards) > 21:
        print("Your opponent went over. You win")
    elif sum(drop_cards) < calculate_score(computer_cards):
        print("You loose.")
    play_a_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()




