# Author: Logan Simonis
# calculating the cost of a road trip
import math
print("Let's see how expensive your trip will be!")
print("")
numMiles = float(input("How many miles will you travel: "))
numDays = int(input("How many days will you be travelling: "))
priceGallon = 3.159
milesGallon = 24.9
breakfastCost = 10
lunchCost = 12.50
dinnerCost = 20.0
hotelCost = 103.25
priceGas = numMiles / milesGallon * priceGallon
travelCost = priceGas + (breakfastCost + lunchCost + dinnerCost + hotelCost) * numDays
print("")
print(f"Travel Cost: ${round(travelCost,2)}")