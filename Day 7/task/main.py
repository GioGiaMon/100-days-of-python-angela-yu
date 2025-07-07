import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"You have to guess {chosen_word}")

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for n in range(len(chosen_word)):
    placeholder=placeholder+"_"
print(f"You have to guess {placeholder}")

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""

for letter in chosen_word:
    if letter == guess:
        # print("Right")
        display=display+letter
    else:
        # print("Wrong")
        display = display + "_"

print(f"Now the word is: {display}")

