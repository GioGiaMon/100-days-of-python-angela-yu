# # Functions with one input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
# Multiple Inputs
# PAUSE 1
# Create a function with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is like in {location}?")



# PAUSE 2
# Modify the function so that it prints the expected values.
# Positional arguments
greet_with("Angela", "Brighton")

# PAUSE 3
# Keyword Arguments
# No matter the position
greet_with(location="London", name="Mary")