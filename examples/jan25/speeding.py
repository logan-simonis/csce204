print("You just got pulled over")
speed = int(input("Enter your speed: "))
if speed > 90:
    print("Go to jail")
elif speed > 80:
    print("Ticket time")
elif speed > 70:
    print("This is a warning!!!")
elif speed < 25:
    print("Jail-You seem to be on drugs!")
elif speed < 45:
    print("Ticket for going too slow")
else:
    print("You are a good person.")
    
print("Have a nice day")