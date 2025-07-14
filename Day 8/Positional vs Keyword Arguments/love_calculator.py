# Love Calculator
# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
## 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
## 2. Then check for the number of times the letters in the word LOVE occurs.
## 3. Then combine these numbers to make a 2 digit number and print it out.
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
###
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
###
# Total = 5
##
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
###
# Total = 3
###
# Love Score = 53
#########
##########  --  Example Input  --- ############
# calculate_love_score("Kanye West", "Kim Kardashian")
############################
# Example Output
# 42
############################################################
# How to test your code and see your output?
#
# Udemy coding exercises do not have a console, so you cannot use the input() function.
# You will need to call your function with hard-coded values like so:
#############
# def calculate_love_score(name1, name2):
#
# # your code here
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")
# example to Count the number of occurrences of a character in a string
# print('Mary had a little lamb'.count('a'))
def calculate_love_score(name1, name2):
    concat_names = name1 + name2
    t_occurrences = int(concat_names.lower().count('t'))
    r_occurrences = int(concat_names.lower().count('r'))
    u_occurrences = int(concat_names.lower().count('u'))
    e_occurrences = int(concat_names.lower().count('e'))
    true_sum = t_occurrences + r_occurrences + u_occurrences + e_occurrences
    l_occurrences = int(concat_names.lower().count('l'))
    o_occurrences = int(concat_names.lower().count('o'))
    v_occurrences = int(concat_names.lower().count('v'))
    e_occurrences = int(concat_names.lower().count('e'))
    love_sum = l_occurrences + o_occurrences + v_occurrences + e_occurrences

    # print(f"Sum of true: {true_sum}, sum of love {love_sum}")
    print(f"{(true_sum * 10) + love_sum}")


# calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score(name1="Angela Yu", name2="Jack Bauer")