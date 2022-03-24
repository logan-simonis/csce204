def get_friends():
    friends = []
    
    with open("examples/mar22/friends.txt") as file:
        for line in file:
            friends.append(line.strip().lower())
            print(line)
        return friends
            

print("Party Time")
people = get_friends()

while True:
    command = input("(C)heck guests, (L)ist guests, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "c":
        name = input("Enter name: ").strip().lower()
        if name in people:
            print("Welcome")
        else:
            print("Sorry, you are not invited")
    elif command == "l":
        print("Friends: ")
        for person in people:
            print(person)
    else:
        print("Invalid command")