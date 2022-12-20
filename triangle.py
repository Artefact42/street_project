import math as m
import turtle as t
from ligne import Ligne

class Triangle :
    def __init__(self, base:int, angle:float, epaisseur:int,couleur_contour:str="black",couleur_fond:tuple or bool or str=False):
        self.b = base
        self.a = angle
        self.c_c = couleur_contour
        self.c_f = couleur_fond
        self.e = epaisseur
    def draw(self):
        l = Ligne(self.b/2/abs(m.cos(self.a*(m.pi/180))), self.e, self.c_c)
        if self.c_f != False :
            t.fillcolor(self.c_f)
            t.begin_fill()
        t.setheading(180-self.a)
        l.draw()
        t.left(self.a*2)
        l.draw()
        if self.c_f != False :
            t.end_fill()