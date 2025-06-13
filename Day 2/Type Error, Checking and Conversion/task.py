# PAUSE 1. Fix the len() function so it has no more warnings or errors.
len("12345")
# PAUSE 2. Write out 4 type checks to print all 4 data types
print(type("abc"))
print(type(12))
print(type(True))
print(type(3.215567))
# Type conversion string to number
print(int("123") + int("45"))
# PAUSE 3. Make this line of code run without errors
username = input("Enter your name: ")
lenUsername = len(username)
print("Number of letters in your name: " + str(lenUsername))
print("Number of letters in your name: " , len(input("Enter your name: ")))