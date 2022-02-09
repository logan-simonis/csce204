# Author: Logan Simonis
# using loops to create hexagons
import turtle
turtle.setup(800,800)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.color("magenta")
pen.width(8)
pen.fillcolor("aqua")
# first hexagon
pen.up()
pen.setpos(110,148)
pen.down()
length = 85
pen.begin_fill()

for i in range(6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()
# second hexagon
pen.up()
pen.setpos(250,230)
pen.down()
length = 85
pen.begin_fill()

for i in range(6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()
# third hexagon
pen.up()
pen.setpos(-28,65)
pen.down()
length = 85
pen.begin_fill()

for i in range(6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()
# fourth hexagon
pen.up()
pen.setpos(-168,-18)
pen.down()
length = 85
pen.begin_fill()

for i in range(6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()
# fifth hexagon
pen.up()
pen.setpos(-308,-100)
pen.down()
length = 85
pen.begin_fill()

for i in range(6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()

turtle.done()