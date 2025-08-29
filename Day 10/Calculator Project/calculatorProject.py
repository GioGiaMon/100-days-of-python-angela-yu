
from art import logo

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
# check the input - number
def check_numeric_input(num):
    isnumeric = False
    while not isnumeric:
        if num.isnumeric():
            isnumeric= True
            num = float(num)
        else:
            num=input("You made a type: please write a valid number\nWhat's the first number?:  ")
    return num

# check the input - operation
def check_input(op, list_to_check, err_log):
    check_op = False
    while not check_op:
        if op in list_to_check:
            check_op = True
        else:
            op=input(f"{err_log}")
    return op


print(logo)
op_list = ['+', '-', '*', '/']
err_msg_op = "You made a type: please write a valid operation.\n+\n-\n*\n/\nPick an operation: "

# # test the divide function - START
# if a.isnumeric():
#     if b.isnumeric():
#         print(divide(float(a),float(b)))
#     else:
#         print("Your second input is not a number")
# else:
#     print("Your first input is not a number")
# # test the divide function - END

# define the dictionary with keys and functions
calculation_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def first_num():
    # ask first number
    a = input("What's the first number?: ")
    # check first number
    return check_numeric_input(a)

# function to ask the operation and the 2nd numbers
def calc_after(num):
    # ask operation
    operation = input("+\n-\n*\n/\nPick an operation: ")
    # check operation
    check_input(operation, op_list, err_msg_op)
    # check operation
    check_input(operation, op_list, err_msg_op)
    # ask for the 2 num
    b = input("What's the next number?: ")
    # check 2 num
    b = check_numeric_input(b)
    # calculate the res
    result = calculation_operations[operation](num, b)
    print(f"{num} {operation} {b} = {float(result)}")
    return result

def go_on(op_result):
    msg_continue = "Type 'y' to continue calculation with " + str(op_result) + " , or 'n' to start a new calculation: "
    how_to_continue = input(msg_continue)
    start_over = check_input(how_to_continue.lower(), ['y', 'n'], "Yuo made a typo.\n" + msg_continue)
    return start_over

restart = 'n'
while restart == 'n':
    a = first_num()
    res = calc_after(a)
    restart = go_on(res)
    while restart == 'y':
        main_result = calc_after(res)
        restart = go_on(main_result)











