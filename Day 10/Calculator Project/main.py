def add(n1, n2):
    return n1 + n2
# PAUSE 1
# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2 !=0:
        return n1/n2
    else:
        return "IMP"

# test the divide function - START
a = input("Type the first number: ")
b = input("Type the second number: ")
if a.isnumeric():
    if b.isnumeric():
        print(divide(float(a),float(b)))
    else:
        print("Your second input is not a number")
else:
    print("Your first input is not a number")
# test the divide function - END

# PAUSE 2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# define the dictionary with keys and functions
calculation_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# PAUSE 3
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# log to start the todo
print("Use the dictionary operations to perform the calculations.\nMultiply 4 * 8 using the dictionary.")
print(calculation_operations['*'](4,8))
