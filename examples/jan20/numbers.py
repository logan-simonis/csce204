# Author: Logan Simonis
import math

# Incrementing Age
age = float(input("Enter Age: "))
decade = 10
futureAge = age + decade
print(f"Your future age is {futureAge}.")

# Pizza Party
print("We're having a Pizza Party!")
numGuests = int(input("Enter number of guests: "))
avgSlices = float(input("Enter Average Slices per Guest: "))
totalSlices = numGuests * avgSlices
numPizzas = math.ceil(totalSlices // 8)

print(f"You should order {numPizzas} pizzas!")

# Chickens and Eggs
numEggs = int(input("How many eggs did you collect today: "))
numCartons = (numEggs // 12)
# eggsLeft = numEggs - numCartons * numEggs
eggsLeft = numEggs % 12 # reamainder after division
print(f"You need {numCartons} cartons.")
print(f"You have {eggsLeft} eggs left over.")

# Wage
hourlyWage = float(input("How much do you get paid hourly: "))
# hourlyWage = hourlyWage * 1.5
hourlyWage *= 1.5
print(f"You should make ${(round(hourlyWage, 2)} in overtime")


