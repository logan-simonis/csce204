# Author: Logan Simonis
# Making debts lists
debts = []
debtValues = []

print("List of Your Debts")
while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "v":
        for debt in debts:
            print(f"- {debt}: ${debtValue}.0")
    elif command == "a":
        debt = input("Enter Debt Name: ")
        debtValue = input("Enter Debt Amount: ")
        debts.append(debt)
        debtValues.append(debtValue)
    elif command == "r":
        print("Sorry, people don't really pay off their debts :)")
    else:
        print("Invalid command")
        
print("Goodbye")