import turtle as t
from rectangle import Rectangle

class Vitre :
    def __init__(self):
        self.e = 1
        self.cote = 30
    def draw(self):
        t.fillcolor("cyan")
        t.begin_fill()
        Rectangle(self.cote, self.cote, self.e).draw()
        t.end_fill()