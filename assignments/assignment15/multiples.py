# Author: Logan Simonis
# making a list of multiples
def displayMultiples():
    number = int(input("Enter Number: " ))
    max = 100
    multiples = []
    for i in range(1, max+1):
        if(i % number) == 0:
            print(i)


while True:
    command = input("(L)ist Multiples, or (Q)uit: ").strip().lower()
    if command == "l":
        displayMultiples()
    if command == "q":
        break

print("Goodbye")