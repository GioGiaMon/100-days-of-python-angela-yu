import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
# write the while loop
# initialize the display word
display = ""
# initialize the attempts and max attempts
attempts = 0
max_attempts = 7
# initialize the guessed letters - correct ones
list_of_guessed = []
# the while loop
while "_" in placeholder and attempts < max_attempts:
    guess = input("Guess a letter: ").lower()
    # check if the attempt is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    #  check if users already catch the letter
    if guess in list_of_guessed:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    # initialize the guessed attempt
    guessed = False
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    # check if guessed or not
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guessed = True
            #  add only the first time!!
            if guess not in list_of_guessed:
                list_of_guessed.append(guess)
    # build the word to display
    for letter in chosen_word:
        if letter in list_of_guessed:
            display += letter
        else:
            display += "_"
    # Add an attempt
    attempts += 1
    if guessed:
        print(f"Good Try! Current word {display}")
        placeholder = display
    else:
        print(f"Wrong guess. Attempts: {attempts}/{max_attempts}\n Current word {display}")
    # initialize the on-going print word variable
    display = ""
    print(f"Attempt number {attempts}, the word: {placeholder}")

# final print out: notify the user the result
if "_" not in placeholder:
    print("🎉 You won!")
else:
    print("💀 You lost!")




