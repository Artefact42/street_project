import turtle as t
from ligne import Ligne

class Rectangle :
    def __init__(self,longueur:int,largeur:int,epaisseur:int,couleur_contour:str="black",couleur_fond:tuple or bool or str=False):
        self.l = longueur
        self.L = largeur
        self.c_c = couleur_contour
        self.c_f = couleur_fond
        self.e = epaisseur
    def draw(self):
        L1 = Ligne(self.l,self.e,self.c_c)
        L2 = Ligne(self.L,self.e,self.c_c)
        angle = 270
        if self.c_f != False :
            t.fillcolor(self.c_f)
            t.begin_fill()
        for i in range(2) :
            t.setheading(angle)
            L2.draw()
            angle-=90
            t.setheading(angle)
            L1.draw()
            angle-=90
        if self.c_f != False :
            t.end_fill()