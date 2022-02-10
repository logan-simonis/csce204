import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

pen.up()
pen.setpos(100,100)
pen.down()
length = 100


#square
pen.fillcolor("magenta")
pen.begin_fill()

for i in range(4):
    pen.forward(length)
    pen.left(90)
    
pen.end_fill()

pen.up()
pen.setpos(-200,100)
pen.down()
pen.begin_fill()
# triangle
for i in range(3):
    pen.forward(length)
    pen.left(120)
pen.end_fill()

pen.begin_fill
# draw a upside down triangle
pen.up()
pen.setpos(-200,-100)
pen.down()

pen.begin_fill
for i in range(3):
    pen.forward(length)
    pen.left(120)
pen.end_fill()


turtle.done()