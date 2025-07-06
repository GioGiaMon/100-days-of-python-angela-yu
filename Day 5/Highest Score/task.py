student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# PAUSE 1 - Max  COMPLETE THIS CHALLENGE WITHOUT USING max()
actual_score = 0
for score in student_scores:
    print("The actual score is: ", score)
    if score > actual_score:
        actual_score = score
        print("Actual highest score is:", actual_score)
print(f"The highest score is: {actual_score}")