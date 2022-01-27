weekDay = input("Enter day of week: ").lower()

if weekDay == "Monday" or weekDay == "mon":
    print("It's Moes Monday!")
elif weekDay == "Wednesday" or weekDay == "Wed":
    print("Pizza Day!")
elif weekDay == "Sunday" or weekDay == "Sun":
    print("Football Hour!")
else:
    print("Sorry, no deal today")