# Author: Logan Simonis
import turtle
import random
turtle.setup(800,800)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.color("black")

colors = ("gold", "hot pink", "spring green", "medium orchid", "lavender", "white")

for i in range(10):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    starWidth = random.randint(20,100)
    starColor = random.choice(colors)
    pen.color(starColor)
    
    pen.circle(starWidth//2)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()
    
    pen.up()
    pen.setpos(x,y+ starWidth / 2)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()
    
    
    




turtle.done()    