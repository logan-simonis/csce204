from datetime import time

assignments = {
    "Assingment 1" : time(9,45),
    "Assignment 2" : time(12, 0),
    "Assignment 3" : time(14,30),
    "Assignment 4" : time(18,45),
    "Assignment 5" : time (22,0)
}

#loop through and display the assignment name,
# and when it's due
for assignment in assignments:
    myTime = assignments[assignment]
    print(f"{assignment}, Due: {myTime.strftime('%M:%H %p')}")
    