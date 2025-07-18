# defining dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
#  retrieve an item from the dictionary
print(f"A bug is: {programming_dictionary["Bug"]}") # spell the key correctly
# add a new entry in dictionary
programming_dictionary["Test"] = "A procedure intended to establish the quality, performance, or reliability of something, especially before it is taken into widespread use."

# check if we add correctly the new element
print(programming_dictionary)

# # wipe the dictionary
# programming_dictionary = {}
# # editing an entry of our dictionary
# programming_dictionary["Bug"] = "New value"
# print(programming_dictionary)

# loop through a dictionary
for item in programming_dictionary:
    # # print the value
    # print(f"{programming_dictionary[item]}")
    # # print the key
    # print(f"{item}")
    # print the key and the value
    print(f"For the key {item} of the dictionary we have this definition: {programming_dictionary[item]}")

