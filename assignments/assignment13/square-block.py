# Author: Logan Simonis
# Looping Square blocks
import turtle
turtle.bgcolor("light blue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

rowsAmount = int(turtle.numinput("Block", "Enter Number of rows ", 5, 1, 10))
count = (rowsAmount)
rows = 1
widthPadding = turtle.window_width()/rowsAmount / 1.15
width = widthPadding * 2/1
padding = widthPadding * .2 
squareWidth = width * .5
squareHeight = width * .5

rowColors = []

for i in range(count):
    colors = (turtle.textinput("Block", f"Enter color of row {rows}:"))
    rowColors.append(colors)
    rows += 1
pen.down()

for row in range(rowsAmount):
    x = -turtle.window_width()/2 + widthPadding / 4
    y = -turtle.window_width()/2 + widthPadding * row + padding

    
    for col in range(rowsAmount):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        for i in range(4):
            if i%2==0:
                pen.forward(squareWidth)
            else:
                pen.forward(squareHeight)
            pen.left(90)
        x += widthPadding

turtle.done()