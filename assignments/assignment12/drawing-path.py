# Author: Logan Simonis
# drawing a star
import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
xList = []
yList = []

coordinateAmount = turtle.numinput("Coordinates", "Enter Number of Coordinates:",5,1,10)
count = int(coordinateAmount)
coordinates = 1
for i in range(count):
    xShape = turtle.numinput("Shapes", f"Enter X {coordinates}")
    yShape = turtle.numinput("Shapes", f"Enter Y {coordinates}")
    xList.append(xShape)
    yList.append(yShape)
    coordinates += 1  
pen.down()
for i in range(len(xList)):
    pen.setpos(xList[i], yList[i])
    
turtle.done()




