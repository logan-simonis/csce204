import turtle
turtle.setup(800,800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

trunkWidth = turtle.window_width() // 10
largeTriangle = trunkWidth * 3
mediumTriangle = largeTriangle * 2/3
smallTriangle = mediumTriangle * 2/3
starWidth = smallTriangle / 2
bottomY = - largeTriangle * 3/2

pen.up()
pen.setpos(-trunkWidth / 2, bottomY)
pen.down()

# draw trunk
pen.color("brown")
pen.begin_fill()

for i in range(4):
    pen.forward(trunkWidth)
    pen.left(90)
      
pen.end_fill()

pen.up()
pen.setpos(-largeTriangle/ 2, bottomY + trunkWidth)
pen.down()
pen.color("forest green")
pen.begin_fill()

# draw big triangle
for i in range(3):
    pen.forward(largeTriangle)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-mediumTriangle/ 2, bottomY + trunkWidth + largeTriangle / 2)
pen.down()
pen.color("forest green")
pen.begin_fill()

# draw medium triangle
for i in range(3):
    pen.forward(mediumTriangle)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-smallTriangle/ 2, bottomY + trunkWidth + largeTriangle / 2 + mediumTriangle / 2)
pen.down()
pen.color("forest green")
pen.begin_fill()

# draw small triangle
for i in range(3):
    pen.forward(smallTriangle)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-starWidth / 2, bottomY + trunkWidth + largeTriangle / 2 + mediumTriangle / 2 + smallTriangle * 0.8)
pen.down()
pen.color("gold")
pen.begin_fill()

# draw star
for i in range(3):
    pen.forward(starWidth)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-starWidth / 2, bottomY + trunkWidth + largeTriangle / 2 + mediumTriangle / 2 + smallTriangle * 0.8 + starWidth / 2)
pen.down()
pen.color("gold")
pen.begin_fill()

# draw star
for i in range(3):
    pen.forward(starWidth)
    pen.right(120)
pen.end_fill()

turtle.done()