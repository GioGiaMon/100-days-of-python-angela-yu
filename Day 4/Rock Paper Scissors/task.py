import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# # user choice - 1 step - input as a string (we can cast the user's choice as an int)
# choice_1 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n")
# # print the user choice 1.1 step
# if choice_1 == "0":
#     print(rock)
# elif choice_1=="1":
#     print(paper)
# elif choice_1=="2":
#     print(scissors)
# else:
#     print("Wrong choice! Maybe a typo...")
#
# # computer choice -> random number - 2 step
# choice_2 = str(random.randint(0,2))
# # print(f"The computer choice: {choice_2}")
# if choice_2 == "0":
#     print(f"Computer chose:\n",rock)
# elif choice_2=="1":
#     print(f"Computer chose:\n",paper)
# elif choice_2=="2":
#     print(f"Computer chose:\n",scissors)
# else:
#     print("Something wrong...maybe a typo...")
# # logic for the result
# # first the draw ...
# if choice_1 == choice_2:
#     print("It's a draw")
# # the user's wins when ->
# elif (choice_1 == "0" and choice_2 == "2") or (choice_1 == "1" and choice_2 == "0") or (choice_1 == "2" and choice_2 =="1"):
#     print("You win!")
# else:
#     print("You loose!")

#  another way -> use a list
game_choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid Number!")
else:
    print(f"Your choice is {game_choice[user_choice]}")
computer_choice = random.randint(0,2)
print("Computer choice:", game_choice[computer_choice])

if computer_choice == user_choice:
    print("It's a draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You loose!")


