import turtle as t
from ligne import Ligne

class Rectangle :
    def __init__(self,longueur:int,largeur:int,epaisseur:int,couleur:str="black"):
        self.l = longueur
        self.L = largeur
        self.c = couleur
        self.e = epaisseur
    def draw(self):
        L1 = Ligne(self.l,self.e,self.c)
        L2 = Ligne(self.L,self.e,self.c)
        angle = 270
        for i in range(2) :
            t.setheading(angle)
            L2.draw()
            angle-=90
            t.setheading(angle)
            L1.draw()
            angle-=90