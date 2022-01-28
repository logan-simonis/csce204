# Author: Logan Simonis
# Making a lady bug

import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")

drawingSize = turtle.numinput("Lady Bug", "Size(1,10)",5,1,10)

largeCircle = 120
mediumCircle = largeCircle * 3/5
eyeSize = mediumCircle * 0.15
spotSize = mediumCircle * 1/6
ladybugSize = drawingSize * turtle.window_height()/5

# medium circle
pen.fillcolor("grey30")
pen.sety(-mediumCircle)
pen.setx(-mediumCircle - 0.5* mediumCircle)
pen.begin_fill()
pen.circle(mediumCircle)
pen.end_fill()

# large circle
pen.fillcolor("red")
pen.up()
pen.setx(-mediumCircle + 1.75 * mediumCircle)
pen.sety(-mediumCircle - 0.68 * mediumCircle)
pen.down()
pen.begin_fill()
pen.circle(largeCircle)
pen.end_fill()

# eyes
pen.fillcolor("white")
pen.up()
pen.sety(-mediumCircle + 0.60 * mediumCircle)
pen.setx(-mediumCircle - 0.95  * mediumCircle)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

pen.fillcolor("white")
pen.up()
pen.sety(-mediumCircle + 1.1 * mediumCircle)
pen.setx(-mediumCircle - 0.95 * mediumCircle)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

pen.pensize(11)
pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.setpos(-largeCircle/1.5,-largeCircle/100)
pen.down()
pen.forward(255)
pen.left(90)

# Spots
pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(largeCircle - 1/2 * largeCircle)
pen.setx(-largeCircle + 1 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()

pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(-largeCircle + 1/2 * largeCircle)
pen.setx(largeCircle + 1 * -largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()

pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(largeCircle - 0.75 * largeCircle)
pen.setx(largeCircle - 0.5 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()

pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(-largeCircle - 0.75 * -largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()

pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(largeCircle + .5 * -largeCircle)
pen.setx(largeCircle - .001 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()

pen.color("grey30")
pen.fillcolor("grey30")
pen.up()
pen.sety(-largeCircle + .5 * largeCircle)
pen.setx(largeCircle - .001 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(spotSize)
pen.end_fill()
turtle.done()