import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# way 1
random_friend = len(friends)-1
print("Today bill got to:", friends[random.randint(0,random_friend)])
# way 2
print(random.choice(friends))
