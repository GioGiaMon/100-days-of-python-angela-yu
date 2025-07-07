import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

#  todo 1
chosen_word = random.choice(word_list)
print(chosen_word)

# todo 2 Ask to guess a letter
guess = input("Guess a letter of the word: ").lower()
if guess.isalpha() and  len(guess)==1:
    print("You Choose", guess)
else:
    print("You made a typo")
# TODO-3 Check if the letter is present in the string
guessed =  chosen_word.find(guess)
if guessed != -1:
    print("Right!")
else:
    print("Wrong")
# # with loop -1
# if guess in chosen_word:
#     print("Right")
# else:
#     print("Wrong")
# for loop - 2
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")



