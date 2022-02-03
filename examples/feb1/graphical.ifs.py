# Learning if statements in graphics

import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("pink")



pen.fillcolor("pink")

shape = turtle.textinput("Shapes, "Enter Shape"). lower().strip()
shapeSize = turtle.window_width()//4

if shape == "cirlce":
    pen.up()
    pen.setpos(0, -shapeSize//2)
    pen.down()
    pen.begin_fill()
    pen.circle(shapeSize//2)
    pen.end_fill()
elif shape == "square":
    pen.up()
    pen.setpos(-shapeSize, -shapeSize//2)
    pen.down()
    pen.begin_fill()
    pen.forward(shapeSize)
    pen.left(90)
    pen.forward(shapeSize)
    pen.left(90) 
    pen.forward(shapeSize)
    pen.left(90)
    pen.forward(shapeSize)
    pen.left(90)
    pen.end_fill()
elif shape == "triangle":
    pen.up()
    pen.setpos(-shapeSize//2, -shapeSize//2)
    pen.down()
    pen.begin_fill()
    pen.forward(shapeSize)
    pen.left(120)
    pen.forward(shapeSize)
    pen.left(120) 
    pen.forward(shapeSize)
    pen.left(120)
    pen.forward(shapeSize)
    pen.left(120)
    pen.end_fill()

turtle.done()