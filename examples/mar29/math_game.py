import random

def get_score():
    with open("examples/mar29/score.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
    return int(lines.pop().strip())

def save_score(score):
    with open("examples/mar29/score.txt", "w") as file:
        file.write(f"{score}\n")
        
def sum_digits(number):
    sum = 0
    
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    
    
    return sum

def play_round():
    randNum = random.randint(1000, 9999)
    ans = sum_digits(randNum)
    
    userAns = int(input(f"Sum the digits of {randNum}: "))
    
    if ans == userAns:
        return True
    else:
        print(f"Incorrect the answer should be {ans}")
        return False
# Read in Score
score = get_score()

#play game and modify score
print("Welcome to Math Fun!")

while True:
    command = input("(P)rint or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command != "p":
        print("Sorry, Invalid command")
        continue
    
    if play_round():
        print("Yay! you got it")
        score += 1
    
    print(f"Your current score is {score}")


#Save score
save_score(score)
