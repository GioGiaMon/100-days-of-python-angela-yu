import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# initialize variables
game_over = False
correct_letters = []
# TODO-1 variable called lives to keep track of the number of lives left. Initialize to 6.
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    # check if guessed -> initialize
    guessed = False

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            guessed = True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if not guessed and lives > 0:
        lives = lives - 1
        # print(f"You have left {lives} tries...")
        # TODO-3: - print the ASCII art from 'stages'
        print(f"{stages[lives]} \nWrong Try! The word to guess: {display}")
        print(f"Your remaining lives are: {lives}")
    elif lives == 0 and not guessed:
        #  no more lives -> end game...
        game_over = True
        # TODO-3: - print the ASCII art from 'stages' - loose ...
        print(f"{stages[lives]} \nYou lose!")
        # print(f"Your remaining lives are: {lives}")
    else:
        # TODO-3: - print the ASCII art from 'stages'
        print(f"{stages[lives]}\nYou guessed a letter! The word to guess is now: {display}")
        # track the remaining attempts
        print(f"Your remaining lives are: {lives}")

    if "_" not in display and lives > 0:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
