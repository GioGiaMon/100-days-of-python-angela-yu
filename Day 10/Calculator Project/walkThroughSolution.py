def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations["*"](4,8))

num1 = float(input("What is the first number?: "))
# print the operation
for op in operations:
    print(op)
operation_symbols = input("Pick an operation: ")
mum2 = float(input("WHat is the next number?: "))
# Program works out the result based on the chosen mathematical operator.
print(operations[operation_symbols])