#Author: Logan Simonis
# making a part list
def getBoolean(item):
    if str(item).lower().strip() in ("true"):
        return True
    if str(item).lower().strip() in ("false"):
        return False
       
def getGuests():
    guest_list = {}   
    with open ("assignments/assignment19/guest_list.txt") as file:
        for line in file:
            data = line.split(':')
            guest = data[0].lower().strip()
            attendances = getBoolean(data[1].strip())
            guest_list[guest] = attendances
        return guest_list
    
guest_names = list(getGuests().keys())
guestAttendance = list(getGuests().values())

def displayGuests(guest, coming):
    if coming == True:
        print("Attending Guest List: ")
        for i in range(len(getGuests())):
            if guestAttendance[i] == True:
                print(f"- {guest_names[i]}")
    elif coming == False:
        print("Not-Attending Guest List: ")
        for i in range(len(getGuests())):
            if guestAttendance[i] == False:
                print(f"- {guest_names[i]}")               
print("Let's Plan our Party")    
while True:
    command = input("View (A)ttending, (N)ot Attending, or (Q)uit: ").strip().lower()
    
    if command == "a":
        displayGuests(guest_names, True)
    elif command == "n":
        print("Not-Attending Guest List: ")
        displayGuests(guest_names, False)
    elif command == "q":
        break
    else:
        print("Sorry, that's an invalid command")
print("Goodbye")