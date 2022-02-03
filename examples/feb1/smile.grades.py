# Grades


eyeRadius = smileRadius //4
mouthRadius = smileRadius //2

# draw head
pen.up()
pen.setpos(0, -smileRadius)
pen.down()
pen.begin_fill()
pen.circle(smileRadius)
pen.end_fill()

# draw left eye
pen.up()
pen.setpos(-smileRadius/3,0)
pen.down()
pen.color("black")
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()


# draw right eye
pen.up()
pen.setpos(smileRadius/3,0)
pen.down()
pen.color("black")
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

pen.up()
pen.color("red")
pen.setpos(-mouthRadius,-mouthRadius * .8)
pen.down()


if grade >= 89.5:
    pen.setheading(-60)
    pen.circle(mouthRadius, 120)  

elif grade >= 69.5:
    pen.forward(mouthRadius * 2)

else:
    pen.up()
    pen.color("red")
    pen.setpos(-mouthRadius * .8,-mouthRadius * .8)
    pen.down()
    pen.setheading(60)
    pen.circle(-mouthRadius, 120) 
   


turtle.done()