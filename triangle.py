import math as m
import turtle as t
from ligne import Ligne

class Triangle :
    """Classe triangle utilisant le module math, turtle et ligne, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le triangle
    """
    def __init__(self, base:int, angle:float, epaisseur:int,couleur_contour:str="black",couleur_fond:tuple or bool or str=False):
        """Methode constructeur
        Prend pour paramètres:
        base:int = Le paramètre correspond à la longueur de la base du triangle isocèle.
        angle:float = Le paramètre correspond aux deux angles de la base.
        epaisseur:int = Le paramètre correspond à l'epaisseur du triangle.
        couleur_contour:str = Le paramètre correspond à la couleur du contour du triangle.
        couleur_fond:tuple or bool or str=False = Le paramètre correpond à la couleur de fond du triangle
        """
        self.b = base
        self.a = angle
        self.c_c = couleur_contour
        self.c_f = couleur_fond
        self.e = epaisseur
    def draw(self):
        """Méthode dessinage du triangle
        Dessine à l'aide des modules math, turtle et ligne. Un triangle en fonction des attributs de la méthode __init__
        """
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