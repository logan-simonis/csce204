# Author: Logan Simonis
# creating a drawing of a bike
import turtle
pen = turtle.Turtle()
pen.pensize(5)
pen.color("black")
# wheel number one
pen.up()
pen.setpos(-100,-58)
pen.down()
pen.fillcolor("aquamarine")
pen.begin_fill()
pen.circle(56)
pen.end_fill()
pen.up()
pen.setpos(0,0)
pen.setheading(0)
pen.down()
# main bike piece
pen.left(60)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.setheading(0)
pen.left(180)
pen.forward(100)
pen.left(240)
pen.forward(100)
pen.up()
pen.setpos(-50,90)
pen.setheading(0)
pen.down()
pen.left(120)
pen.forward(50)
pen.left(60)
pen.forward(30)
pen.left(180)
pen.forward(50)
pen.up()
pen.setpos(50,90)
pen.down()
pen.left(105)
pen.forward(45)
pen.left(75)
pen.forward(25)
pen.up()
pen.setpos(50,90)
pen.down()
pen.left(120)
pen.forward(100)
# wheel number two
pen.up()
pen.setpos(50,-30)
pen.down()
pen.fillcolor("aquamarine")
pen.begin_fill()
pen.circle(55)
pen.end_fill()









turtle.done()
