import random
# test for understanding random and modules
# import my_module
#
# random_int = random.randint(1,10)
# print(random_int)
#
# print(my_module.my_favorite_number)

# # create a floating point number 0=< x < 1
# random_number = random.random()
# print(random_number)

# # random floating point generator
# random_float = random.uniform(1,10)
# print(random_float)
print("Flipping a coin...\nWait the result..")
flip_coin_result = random.randint(1,2)
if flip_coin_result == 2:
    print("\nHead")
else:
    print("\nTail")