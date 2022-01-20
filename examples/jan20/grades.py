# Calculate Grades
print("Let's calculate your grade")
assignmentsGrade = float(input("Assignments: "))
exerciseGrade = float(input("Exercises: "))
midtermGrade = float(input("Midterm: "))
finalGrade = float(input("Final: "))

classGrade = assignmentsGrade * .55 + exerciseGrade * .15 + midtermGrade * .15 + finalGrade * .15

print(f"Your Grade is {round(classGrade, 1)}.")

