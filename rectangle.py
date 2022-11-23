import turtle as t
from ligne import Ligne

class Rectangle :
    def __init__(self,longeur:int,largeur:int,epaisseur:int,couleur:str="black"):
        self.l = longeur
        self.L = largeur
        self.c = couleur
        self.e = epaisseur
        self.a = 90
    def draw(self):
        t.pencolor(self.c)
        t.pensize(self.e)
        for i in range(2) :
            t.forward(self.l)
            t.left(self.a)
            t.forward(self.L)
            t.left(self.a)