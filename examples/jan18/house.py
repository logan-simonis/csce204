import turtle   # making a house
turtle.bgcolor("light blue")
pen = turtle.Turtle()

pen.pensize(10)
# draw a hosue
pen.up()
pen.setpos(-100,-100)
pen.down()

pen.fillcolor("dark blue")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()

# draw roof triangle
pen.up()
pen.setpos(-100,100)
pen.down()
pen.setheading(0)
pen.left(65)
pen.forward(200)
pen.right(122)
pen.forward(205)

# make a door
pen.up()
pen.setpos(-25, -100)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.setheading(0)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

# draw a tree
pen.up()
pen.setpos(250,-150)
pen.down()
pen.fillcolor("saddle brown")
pen.begin_fill()
pen.setheading(0)
pen.forward(30)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.end_fill()









turtle.done()