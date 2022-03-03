import turtle
import random
turtle.setup(800,800)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("sky blue")

def draw_square(x, y, width, color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()
    
def draw_triangle(x, y, width, color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

#test
draw_square(50, -100, 60, "cyan")
draw_triangle(-100, 200, 50, "pink")
#draw_square(20, 50, 80, "pink")
#draw_square(-20, -50, 100, "red")
#draw_square(-50, -50, 40, "blue")

turtle.done()
