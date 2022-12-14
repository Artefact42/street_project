import turtle as t
from sol import Sol
#from immeuble import Immeuble
from rectangle import Rectangle

class Rue :
    def __init__(self) :
        self.ox = -355
        self.oy = -160
        self.esp = 30
        
    def draw (self):
        t.penup()
        t.goto(self.ox, self.oy)
        t.pendown()
        Sol().draw()
        t.penup()
        t.goto(self.ox, self.oy)
        for i in range(4):
            self.ox +=170
            t.penup()
            t.goto(self.ox, self.oy)
            t.pendown()
            Rectangle(140,140,5).draw()