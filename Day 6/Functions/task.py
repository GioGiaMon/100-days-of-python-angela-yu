print("Hello")
num_char = len("Hello")
print(num_char)

#  my own function
def my_function():
    print("Hello")
    print("Bye")

# # call the function
# my_function()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()




# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Reeborg's world
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
# def block():
#     move()
#     jump()
#     turn_left()
#
# block()
# block()
# block()
# block()
# block()
# block()

# angela solution
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for step in range(6):
#     jump

# RObot Hurdle 2 challenge
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#
#
# def block():
#     move()
#     jump()
#     turn_left()
#
#
# while not at_goal():
#     block()


# Challenge Hurdle 3:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#
#
# def block():
#     move()
#     jump()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()
#         turn_left()

# Challenge Hurdle 4:
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     else:
#         turn_right()
#         move()
#         turn_right()
#     while front_is_clear():
#         move()
#
# while not at_goal():
#   if front_is_clear():
#     move()
#   elif wall_in_front():
#     jump()
#     turn_left()
# Maze challenge
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
# while not at_goal():
#    turn_right()
#    if not wall_in_front():
#         move()
#    else:
#     turn_left()
#     if not wall_in_front():
#         move()
#     else:
#         turn_left()
#         if front_is_clear():
#             move()

#
#
# Maze challenge v2
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
# while front_is_clear():
#    move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()