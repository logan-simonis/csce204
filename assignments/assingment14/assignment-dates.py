# Author: Logan Simonis
# Assignments and their due dates
from datetime import date

assignments = {
    "Ass 1 - Intro": date(22,12,7),
    "Ass 2 - Mad Libs": date(22,12,5),
    "Ass 3 - Bike": date(22,12,8),
    "Ass 4 - Prices": date(22,2,12),
    "Ass 5 - Lady Bug": date(22,2,24),
    "Ass 6 - Zodiac Signs": date(22,2,27),
    "Ass 7 - Reading Race": date(22,3,7),
    "Ass 8 - Count Factors": date(22,3,15),
    "Ass 9 - Hexagon": date(22,3,24),
    "Ass 10 - Shoes": date(22,3,28)
}

for assignment in assignments:
    myTime = assignments[assignment]
    if myTime == date(22,12,7):
        print(f"- {assignment} - {myTime.strftime('%b %d, %A')} - Due Today!")
    if myTime == date(22,12,5):
        print(f"- {assignment} - {myTime.strftime('%b %d, %A')} - 2 Days Past Due!")
    if myTime == date(22,12,8):
        print(f"- {assignment} - {myTime.strftime('%b %d, %A')} - Due in 1 Day!")      
    else:
        print(f"- {assignment} - {myTime.strftime('%b %d, %A')}")