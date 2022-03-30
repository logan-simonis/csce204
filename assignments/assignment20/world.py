import turtle
turtle.setup(300,300)
pen = turtle.Turtle()
pen.speed(0)
turtle.bgcolor("light blue")
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneItems = []
    with open("assignments/assignment20/scene.txt") as file:
        for line in file:
            sceneItem = line.replace("\n", "").strip().lower()
            sceneItems.append(sceneItem)       
        return sceneItem    
def drawFlower(x, y, size):
    pen.up()
    pen.setpos(x,y)
    pen.setheading(0)
    pen.down()
    pen.color("green")
    pen.left(90)
    pen.forward(size*2.5)
    pen.color("pink")
    counter = 0
    for f in range(20):
        pen.circle(size/1.5)
        counter += 5
        pen.left(counter)
def drawTree(x, y, size):
    pen.up()
    pen.setpos(x,y)
    pen.setheading(0)
    pen.down()
    pen.color("brown")
    pen.begin_fill()
    for i in range(2):
        pen.forward(size/2)
        pen.left(90)
        pen.forward(size*2)
        pen.left(90)
    pen.end_fill()
    pen.color("green")
    pen.begin_fill()
    pen.up()
    pen.setpos(x+size/4, y+size*1.25)
    pen.down()
    pen.circle(size*1.5)
    pen.end_fill()    
counter = 0
Scene = getScene()
allItems = len(Scene)
x = turtle.window_width()/allItems
y = turtle.window_height()/2
size = turtle.window_width()/1.5/allItems
for i in range(allItems):
    if Scene[i] == "flower":
        drawFlower(x*counter,y,size)
        counter += 3
    elif Scene[i] == "tree":
        drawTree(x*counter,y,size)
        counter += 3

turtle.done()