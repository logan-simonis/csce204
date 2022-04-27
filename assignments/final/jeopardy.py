# Author: Logan Simonis
from question import Question
import turtle
import random
turtle.setup(600,600)
pen1 = turtle.Turtle()
pen1.hideturtle()
pen2 = turtle.Turtle()
pen2.hideturtle()
pen3 = turtle.Turtle()
pen3.hideturtle()
font = ("courier", 22, "bold")
pen1.up()
pen2.up()
pen3.up()
pen3.setpos(-25,-120)
def getQuestions():
    questions = []
    with open("assignments/final/questions.txt") as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions.append(Question(question, answer))
        return questions  
     
def displayQuestion(question):
    pen1.setpos(-235,0)
    pen1.write(question.get_question(), font = font)
    pen1.setpos(-165,-100)
    pen1.write("Incorrect Guesses", font=font)
def displayAnswerFragment(question):
    pen2.setpos(-145, -30)
    pen2.write(question.getAnswerFragment(), font=font)
def correctAnswer():
    emptyLetter = 0
    for letter in question.answer_fragment:
        if letter == "_":
            emptyLetter += 1
        else:
            continue
    
    if emptyLetter == 0:
        pen2.clear()
        pen1.clear()
        pen3.clear()
        pen1.setpos(-200,0)
        pen1.write(f"Congrats You Won!", font = font)
        pen1.setpos(-200,-50)
        pen1.write(f"Correct Answer: {question.get_answer().upper()}", font = font)
def userGuess(x, y):
    global question
    if isinstance((x+y), float) == True:
        guess = turtle.textinput("Guess", "Enter Letter: ")
        if question.guess(guess) == True:
            pen2.setpos(-80,-30)
            pen2.clear()
            pen2.write(question.getAnswerFragment(), font=font)
        else:
            pen3.forward(30)
            pen3.write(guess.upper(), font = font)
    correctAnswer()

questions = getQuestions()
question = random.choice(questions)

displayQuestion(question)
displayAnswerFragment(question)
turtle.onscreenclick(userGuess)
turtle.done()