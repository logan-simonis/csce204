# Author: Logan Simonis
# Counting Factors

print("Let's Count Factors")
num = int(input("Enter Number: "))

counter = 1

while counter <= num:
    if(num % counter ==0):
        print("{0}".format(counter))
    counter = counter+1
