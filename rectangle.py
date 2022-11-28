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
        L1 = Ligne(self.l,self.e,self.c)
        L2 = Ligne(self.L,self.e,self.c)
        for i in range(2) :
            L1.draw()
            t.right(self.a)
            L2.draw()
            t.right(self.a)