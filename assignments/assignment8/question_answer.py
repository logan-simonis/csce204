# Author: Logan Simonis
# Making a Question Answering Game
print("Welcome to our Question Answer Game")
theQuestion = input("Ask a yes or no question: ")
answers = (1,3)
if answers == 1:
    print("Yes")
elif answers == 2:
    print("No")
elif answers == 3:
    print("Maybe")
    
command = input("Would you like to ask another question? (Y)es or (N)o: ").lower().strip()
while command == input("y").lower().strip():
    
        theQuestion = input("Ask a yes or no question: ")
        if answers == 1:
            print("Yes")
        elif answers == 2:
            print("No")
        elif answers == 3:
            print("Maybe")
    
else: print("Goodbye")
    
