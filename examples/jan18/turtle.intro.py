import turtle   # first line of every turtle program
turtle.bgcolor("light sea green")
pen = turtle.Turtle()

pen.pensize(10)
pen.color("dark red")
pen.forward(200)

# How to make a square
pen.begin_fill()
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()

# Triangle
pen.up()
pen.setpos(-200,150)
pen.down()
pen.setheading(0)
pen.color("dark blue")
pen.begin_fill()
pen.forward(150)
pen.left(120)
pen.forward(150)
pen.left(120)
pen.forward(150)
pen.left(120)
pen.end_fill()








turtle.done()   # last line of every turtle program