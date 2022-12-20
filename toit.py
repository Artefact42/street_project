from random import randint
from demi_cercle import Demi_cercle
import turtle as t
from triangle import Triangle

class Toit:
    def __init__(self):
        self.type = randint(1,2)
        self.e = 3
        self.l = 140
        self.c = "brown"
        self.angle = 45
        self.nb_ronds = 5
    def draw(self):
        if self.type == 1:
            Triangle(self.l, self.angle, self.e, couleur_fond=self.c).draw()
        elif self.type == 2:
            for i in range(self.nb_ronds):
                t.setheading(90)
                Demi_cercle(self.l/self.nb_ronds, self.e, couleur_fond=self.c).draw()