class Boat:
    def __init__(self, x, y, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        
    def draw(self, pen):
        pen.up()
        pen.setpos(self.x - self.height/2, self.y - self.height/2)
        pen.down()
        pen.fillcolor(self.color)
        
        self.draw_frame(pen)
        self.draw_pole(pen)
        self.draw_flag(pen)
            
    def draw_frame(self, pen):
        pen.up()
        pen.setpos(self.x, self.y)
        pen.down()
        pen.begin_fill()
        pen.forward(self.height)
        pen.left(-120)
        pen.forward(self.height * .5)
        pen.left(-60)
        pen.forward(self.height * .8)
        pen.left(-60)
        pen.forward(self.height * .5)
        pen.left(-60)
        pen.end_fill()
        
    def draw_pole(self, pen):
        pen.left(-60)
        pole_width = self.height * .05
        pole_height = pole_width * 12
        pen.up()
        pen.setpos(self.x + 35, self.y)
        pen.down()
        pen.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                pen.forward(pole_width)
            else:
                pen.forward(pole_height)
            pen.left(90)
        pen.end_fill()
        
    def draw_flag(self, pen):
        pen.up()
        pen.left(90)
        pen.setpos(self.x + 35, self.y + 30)
        pen.down()
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.height/3.5)
            pen.left(120)
        pen.end_fill()
        pen.left(-90)