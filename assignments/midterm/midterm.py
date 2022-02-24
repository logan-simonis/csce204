# Author: Logan Simonis
# creating stars in the sky
import turtle
import random
turtle.bgcolor("black")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

starsAmount = int(turtle.numinput("Amount of Stars", "How many stars do you have? ", 5, 1, 10))
count = (starsAmount)
rows = 1
widthPadding = turtle.window_width()/starsAmount / 3
padding = widthPadding * .2 
length = 100 / starsAmount
width = widthPadding * .8
style = ("Arial", 18, "normal")

starNames = []
starColors = []

pen.up()
pen.setpos(-250,225)
pen.color("white")
pen.begin_fill()
pen.write("Beautiful Stars", font = style, align = "left")
pen.down()
pen.end_fill()

for i in range(count):
    starName = (turtle.textinput("Names", f"Enter name of star {rows}:"))
    starColor = (turtle.textinput("Colors", f"Enter color of star {rows}:"))
    starNames.append(starName)
    starColors.append(starColor)
    rows += 1
pen.down()



for row in range(starsAmount):
    x = random.randint(- int(turtle.window_height()/2 + widthPadding /2), 300)
    y = random.randint(- int(turtle.window_height()/4 + widthPadding + widthPadding * row + padding), 100)
    
    for col in range(starsAmount):
        pen.up()
        pen.setpos(x,y+20)
        pen.begin_fill()
        pen.color("white")
        pen.write(starNames[row], font = style)
        pen.down()
        pen.end_fill()
        pen.color(starColors[row])
        
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.begin_fill()    
        for j in range(3):
            pen.forward(length)
            pen.left(120)
        pen.end_fill()
            

        pen.up()
        pen.setpos(x + length,y + length/1.75)
        pen.down()
        pen.begin_fill()
        for j in range(3):
            pen.forward(-length)
            pen.left(120)
        pen.end_fill()
    x += widthPadding

turtle.done()