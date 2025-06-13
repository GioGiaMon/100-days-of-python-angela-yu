print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
onePay = (bill/people)*((tip/100)+1)
# print("Each person should pay: $", round(onePay,2))
print(f"Each person should pay: ${round(onePay,2)}")


