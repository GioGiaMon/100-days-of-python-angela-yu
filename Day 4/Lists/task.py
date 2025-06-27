import random

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[-2]) # Apple
print(fruits[0]) # Cherry
random_fruits = random.randint(0,2)
print("Random fruits:", fruits[random_fruits])
fruits.append("Strawberry") # at the end of the list ++
random_fruits = random.randint(0,3)
print("New Random fruits:", fruits[random_fruits])
fruits.extend(["Blueberry", "Orange", "Banana"]) # adds the specified list elements (or any iterable) to the end of the current list.
random_fruits = random.randint(0,6)
print("New Random fruits:", fruits[random_fruits])
