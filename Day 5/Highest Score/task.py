student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# PAUSE 1 - Max -> write the code without ht built-in function max
actual_score = 0
for score in student_scores:
    if score > actual_score:
        actual_score = score
        # print(f"Actual score {actual_score}, now we are at {score}")
print(f"The max score of the students is {actual_score}")
