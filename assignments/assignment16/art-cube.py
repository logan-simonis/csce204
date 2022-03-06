# Author: Logan Simonis
# Making art with cubes
import turtle
import random

turtle.setup(600,600)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

shape_color = ["green", "yellow", "red", "black", "pink", "blue", "orange","salmon"]

def triangle(x, y, width, shape_color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(random.choice(shape_color))
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def art_cube(x, y, size, shape_color):
    for i in range(6):
        triangle(x, y, size, shape_color)
        pen.left(60)
        

for i in range(20):
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2)) 
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))   
    size = random.randint(20,80)    
    art_cube(x, y, size, shape_color)

turtle.done()