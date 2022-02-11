# Author: Logan Simonis
# creating a list with loops
shoes = []
print("Shoe Inventory")


while True:
    command = input("Do you have more shoes to add, (Y)es or (N)o: ").strip().lower()
    
    if command == "n":
        print("Here's your shoe inventory list: ")
        for shoe in shoes:
            print(f"- {shoe}")
    elif command == "y":
        shoe = input("Enter Shoe Name: ")
        shoes.append(shoe)     
    else:  
        print("Invalid command")


    

