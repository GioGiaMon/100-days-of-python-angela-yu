print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go?")
direction = input("Type ""left"" or ""right""\n ")
if direction.lower() == "left":
    print("You've come to a lake.\nThere is an island on the middle of the lake.")
    action = input("Type ""wait"" to wait for a both.\nType ""swim"" to swim across.")
    if action.lower() == "wait":
        print("You arrived at the island unharmed. There is an house with 3 doors.")
        color = input("One red, one yellow and one blue. Which color do you choose?")
        if color.lower() == "red":
            print("Burn by fire. Game Over")
        elif color.lower() == "blue":
            print("Eaten by beast. Game Over")
        elif color.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
