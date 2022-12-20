import turtle as t
from rectangle import Rectangle
from demi_cercle import Demi_cercle
from ligne import Ligne
from random import randint

class Porte :
    def __init__(self):
        self.type = randint(1,2)
        self.e = 1
        self.l = 30
        self.L = 45
        self.diminution_porte2 = 5
    def draw(self):
        if self.type == 1 :
            Rectangle(self.l,self.L,self.e,couleur_fond="sienna").draw()
        else :
            t.fillcolor("cyan")
            t.begin_fill()
            t.setheading(270)
            Ligne(self.L-self.diminution_porte2,self.e).draw()
            t.setheading(0)
            Ligne(self.l,self.e).draw()
            t.setheading(90)
            Ligne(self.L-self.diminution_porte2,self.e).draw()
            t.setheading(90)
            Demi_cercle(self.l,self.e).draw()
            t.end_fill()