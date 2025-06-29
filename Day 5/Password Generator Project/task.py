import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version - Generate the password in sequence. Letters, then symbols, then numbers
# get random elements from the arrays
password_letters = random.choices(letters, k=nr_letters)
password_number = random.choices(numbers, k=nr_numbers)
password_symbols = random.choices(symbols, k=nr_symbols)
# create the password
pass_init=""
for l in password_letters:
    pass_init = pass_init + l
for n in password_number:
    pass_init = pass_init + n
for s in password_symbols:
    pass_init = pass_init + s
print("Your Password - easy - is: ", pass_init)

# Hard Version - the final password does not follow a pattern.
# make a unique array
# password_mix = password_letters.copy()
# password_mix.extend(password_number)
# password_mix.extend(password_symbols)
# random.shuffle(password_mix)
# password = ''.join(password_mix)
# print("Your Password - hard - is:", password)
pass_mix = []
# make a unique array
pass_mix.extend(password_letters)
pass_mix.extend(password_number)
pass_mix.extend(password_symbols)
# shuffle the new list
random.shuffle(pass_mix)
print(pass_mix)
password = ''.join(pass_mix)
print("Your Password - hard - is:", password)










