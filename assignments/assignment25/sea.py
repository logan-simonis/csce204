from boat import Boat
import turtle
import random
turtle.setup(575,575)
turtle.bgcolor("dodger blue")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colors = ["yellow", "green", "pink", "gold", "purple", "dark blue", "aquamarine", "magenta"]
boat_color = random.randint(0,7)

boats = []

for i in range(10):
    boats.append(Boat(random.randint(-300,200), random.randint(-300,200), random.randint(75,100), colors[random.randint(0,7)]))

for boat in boats:
        boat.draw(pen)
    
turtle.done()