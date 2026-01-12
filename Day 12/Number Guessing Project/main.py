import random
from art import logo

# function to select the number from 1 to 100
def pick_a_number():
    my_range = range(1,101)
    # print(f"{my_range[0]} {my_range[99]}")
    picked_number = random.choice(my_range)
    print(f"the number chosen is {picked_number}")
    return picked_number

def game_difficulty():
    #  ask the difficulty until the input is valid...
    while True:
        difficulty = input("Choose a difficulty: type 'hard' or 'easy': ")
        if difficulty.lower() == 'easy':
            attempts = 10
            print(f"The difficulty chosen is {difficulty}: so the attempts are {attempts}")
            return attempts
        elif difficulty.lower() == 'hard':
            attempts = 5
            print(f"The difficulty chosen is {difficulty}: so the attempts are {attempts}")
            return attempts
        else:
            print(f"You wrote an invalid difficulty. Try again.")

def get_guess():
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")


def game_run():
    # intro
    print(logo)
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking a number between 1 and 100.")
    # fist computer pick up a number
    number_chosen = pick_a_number()
    #  second select the difficulty
    attempts = game_difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_try = get_guess()
        if user_try == number_chosen:
            print(f"You got it! The answer was {user_try}")
            break
        elif user_try > number_chosen:
            print(f"Too high.\nGuess again.")
            attempts = attempts - 1
        elif user_try < number_chosen:
            print(f"Too low.\nGuess again.")
            attempts = attempts - 1
    print(f"You've run out of guesses.The number was {number_chosen}. You lose.")

game_run()




