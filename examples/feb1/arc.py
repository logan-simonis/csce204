# Learning if statements in graphics

import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("pink")

arcRadius = 100

# smile arc
pen.up()
pen.setpos(-arcRadius, 0)
pen.down()
pen.setheading(-60)
pen.circle(arcRadius, 120)

# frow
pen.up()
pen.setpos(0, 0)
pen.down()
pen.setheading(60)
pen.circle(-arcRadius, 120)




turtle.done()