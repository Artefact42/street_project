import turtle as t
from ligne import Ligne
from random import *
from rectangle import Rectangle
class Etage:
    def __init__(self):
        self.h = 60
        self.L = 140
        self.e = 3
        self.type = randint(0,3)
        self.couleur = ["blue","red","green","yellow","brown","pink","orange","purple"]
    def draw(self):
        if self.type == 0:
            t.fillcolor(choice(self.couleur))
            t.begin_fill()
            Rectangle(self.L,self.h,self.e).draw()
        if self.type == 1:
            for i in range(2):
                t.fillcolor(choice(self.couleur))
                t.begin_fill()
                Rectangle(self.L,self.h,self.e).draw()
                self.h += 60
                t.end_fill()
        if self.type == 2:
            t.fillcolor(choice(self.couleur))
            t.begin_fill()
            Rectangle(self.L,self.h,self.e).draw()
            Rectangle(self.L,self.h+60,self.e).draw()
            Rectangle(self.L,self.h+120,self.e).draw()
            t.end_fill()
        if self.type == 3:
            t.fillcolor(choice(self.couleur))
            t.begin_fill()
            Rectangle(self.L,self.h,self.e).draw()
            Rectangle(self.L,self.h+60,self.e).draw()
            Rectangle(self.L,self.h+120,self.e).draw()
            Rectangle(self.L,self.h+180,self.e).draw()
            t.end_fill()