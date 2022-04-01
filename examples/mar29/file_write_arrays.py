def read_friends():
    friends = []
    with open("examples/mar29/friends.txt") as file:
        for line in file:
            friends.append(line.strip())
    return friends

def write_friends(friends):
    with open("examples/mar29/friends.txt", "w") as file:
        for friend in friends:
            file.write(f"{friend}\n")

def display_friends(friends):
    for friend in friends:
        print(f"- {friend}")
        
# main prpgram    
friend_list = read_friends()
#modify list
print("Hey Friends!")

while True:
    command = input("(A)dd, (D)elete, (V)iew, (Q)uit: ")
    
    if command == "q":
        break
    elif command == "v":
        display_friends(friend_list)
    elif command == "a":
        friend = input("Enter friend name: ")
        friend_list.append(friend)
        print(f"{friend} was added to the list.")

print("Goodbye")



#Save List
write_friends(friend_list)
