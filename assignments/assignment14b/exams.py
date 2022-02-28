# Author: Logan Simonis
# Exams and their times
from datetime import date, time, datetime


classes = {
    "CSCE 204": datetime(22, 2, 27, 8, 30),
    "ENVR 101": datetime(22, 3, 2, 1, 45),
    "ITEC 265": datetime(22, 2, 27, 3, 15),
    "ITEC 245": datetime(22, 2, 27, 9, 45),
    "CSCE 240": datetime(22, 3, 20, 11, 30),
    "ITEC 101": datetime(22, 4, 5, 2, 50),
    "ENVR 101L": datetime(22, 3, 15, 12, 00)
}

for name in classes:
    myTime = (classes[name])
    thedate = datetime.today()
    if datetime.today().date() == thedate.date():
        print("Todays Exams:")
        print(f"{myTime.strftime('%I:%M %p')} {name}")
    print()
    if datetime.today().date() < thedate.date():
        print("Upcoming Exams:")
        print(f"{myTime.strftime('%I:%M %p')} {name}")        