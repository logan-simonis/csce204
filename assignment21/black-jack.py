# Author: Logan Simonis
import random
def getScore():
    with open("assignments/assignment21/scores.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        return lines.pop()

def save_score(score):
    with open("assignments/assignment21/scores.txt", "w") as file:
        file.write(f"Your current score is {score}\n")

def play_round():
    point = ""
    drawOne = int(randNum)
    drawTwo = int(randNum)
    total = drawOne + drawTwo
    computerTotal = random.randint(14,23)
    randNum = random.randint(1, 11)
    print(f"Your Hand Total: {total}")

    while True:
        while total < 21:
            command = input("Do you want another card (Y)es or (N)o: ").strip().lower()
    
            if command == "n":
                break
            elif command == "y":
                while command == "y":
                    randNum = random.randint(1,11)
                    total += int(randNum)
                    print(f"You drew a {randNum}\nYour hand totals: {total}")
                    break
            else:
                print("Invalid Command")

        if total == computerTotal or (total > 21 and computerTotal > 21):
            print(f"Computer's hand total: {computerTotal}\nYou tied")
            point = 0
        elif total < 21 and total > computerTotal:
            print(f"Computer's hand total: {computerTotal}\nYou win")
            point = 1
        elif total < computerTotal and computerTotal > total:
            print(f"Computer's hand total: {computerTotal}\nYou lose")
            point = -1
        return True

print("Let's Play Black Jack \n")
score = getScore()
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        print(f"Your score is {score}")
        break
    elif command != "p":
        print("Sorry, Invalid command")
        continue
    
    if play_round():
        score += 1
    
print("goodbye")
save_score(score)