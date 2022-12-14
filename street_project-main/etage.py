import turtle as t
from random import randint
from rectangle import Rectangle
from porte import Porte
from fenetre import Fenetre

class Etage:
    def __init__(self, couleur:tuple, rdc:bool):
        self.h = 60
        self.L = 140
        self.e = 1
        self.c = couleur
        self.rdc = rdc
    def draw(self):
        if self.rdc :
            posx = t.pos()[0]
            posy = t.pos()[1]
            
            position_porte = randint(0,2)
            t.fillcolor(self.c)
            t.begin_fill()
            Rectangle(self.L,self.h,self.e).draw()
            t.end_fill()
            for i in range (3) :
                t.penup()
                if position_porte == i :
                    posx -=15
                    posy -=15
                    t.goto(posx, posy)
                    t.pendown()
                    Porte().draw()
                else :
                    Fenetre().draw()

        else :
            t.fillcolor(self.c)
            t.begin_fill()
            Rectangle(self.L,self.h,self.e).draw()
            t.end_fill()
            for i in range (3) :
                Fenetre().draw()
                
                
