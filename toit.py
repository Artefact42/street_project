from random import randint
from rectangle import Rectangle
from demi_cercle import Demi_cercle
import turtle as t
from ligne import Ligne


class Toit:
    def __init__(self):
        self.type = randint(1,2)
        self.e = 3
        self.l = 20000**0.5
        self.d = 200
    def draw(self):
        if self.type == 1:
            t.fillcolor("brown")
            t.begin_fill()
            t.setheading(135)
            Ligne(self.l,self.e).draw()
            t.setheading(-135)
            Ligne(self.l,self.e).draw()
            t.end_fill()
        elif self.type == 2:
            for i in range(5):
                t.setheading(90)
                Demi_cercle(self.d/5, self.e,couleur_fond="brown").draw()