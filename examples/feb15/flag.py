# Author: Logan Simonis
import turtle
turtle.setup(800,600)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("red")

x = - turtle.window_width()//2
y = - turtle.window_height()//2
stripeWidth = turtle.window_width()
stripeHeight = turtle.window_height()/13

# draw red stripes
for i in range(7):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    # draw stripe
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0: #if i is even
            pen.forward(stripeHeight)
        else:
            pen.forward(stripeHeight)
        pen.left(90)
    pen.end_fill()
    
    y += stripeHeight * 2 #move up for next stripe

# blue square
blueSquareWidth = turtle.window_width() //2.5
blueSquareHeight = turtle.window_height() * 7/13
x = - turtle.window_width() //2
y = - turtle.window_height()//2 + (turtle.window_height() - blueSquareHeight)
pen.up()
pen.setpos(x,y)
pen.down()

pen.begin_fill()
for i in range(4):
    if i % 2 == 0: 
            pen.forward(blueSquareWidth)
    else:
        pen.forward(blueSquareHeight)
        pen.left(90)
pen.end_fill()


    
    
    
    








turtle.done()