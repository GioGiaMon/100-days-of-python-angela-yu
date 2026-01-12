from random import randint

# global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to Check users' guess  against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return 0

# function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty: type 'hard' or 'easy': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # set the difficulty
    turns = set_difficulty()


    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        # Let the user guess a number but before show the number of  attempts
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        # Check the answer
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses. The number was {answer}. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Track the number of attempts and reduce by 1 if they get it wrong

game()



