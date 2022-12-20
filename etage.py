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
        origine = t.pos()
        if self.rdc :
            position_porte = randint(0,2)
            Rectangle(self.L,self.h,self.e,couleur_fond=self.c).draw()
            t.penup()
            for i in range (3):
                if i == position_porte :
                    p = Porte()
                    if p.type == 1 :
                        t.goto(origine[0]-(15+i*40),origine[1]-self.h+p.L)
                        t.pendown()
                        p.draw()
                    else:
                        t.goto(origine[0]-(15+i*40+p.l),origine[1]-self.h+p.L-p.diminution_porte2)
                        t.pendown()
                        p.draw()
                    t.penup()
                else :
                    t.goto(origine[0]-(15+i*40),origine[1]-8)
                    t.pendown()
                    Fenetre().draw()
                    t.penup()
        else :
            Rectangle(self.L,self.h,self.e,couleur_fond=self.c).draw()
            t.penup()
            for i in range(3):
                t.goto(origine[0]-(15+i*40),origine[1]-8)
                t.pendown()
                Fenetre().draw()
                t.penup()