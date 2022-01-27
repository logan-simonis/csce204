assignments = float(input("Assignments: "))
exercises = float(input("Exercises: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

classGrade = assignments * .55 + exercises * .15 + midterm * .15 + final * .15

print(f"Your class Grade is {round(classGrade, 1)}%.")

letter = "F"

if classGrade >= 89.5:
    letter = "A"
elif classGrade >= 79.5:
    letter = "B"
elif classGrade >= 69.5:
    letter = "C" 
elif classGrade >= 59.5:
    letter = "D"

print(f"You earned a(n) {letter}.")