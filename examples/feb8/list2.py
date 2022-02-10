toys = ["car", "plane", "racecar", "trampoline", "legos"]

print("Welcome to our toy store")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "v":
        for toy in toys:
            print(f"- {toy}")
    elif command == "a":
        toy = input("Enter Toy: ")
        toys.append(toy)
        print(f"{toy} was added")
    elif command == "r":
        toy = input("Enter Toy: ")
        toys.remove(toy)
    else:
        print("Invalid command")
    
 



print("Goodbye")