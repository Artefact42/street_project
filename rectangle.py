import turtle as t
from ligne import Ligne

class Rectangle :
    """Classe Rectangle utilisant le module turtle, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le Rectangle
    """
    def __init__(self,longueur:int,largeur:int,epaisseur:int,couleur_contour:str="black",couleur_fond:tuple or bool or str=False):
        """Methode constructeur de la classe Rectangle
        longueur:int = Longueur du Rectangle en entier naturel.
        largeur:int = Largeur du Rectangle en entier naturel.
        epaisseur:int = Epaisseur du rectangle en entier naturel.
        couleur_contour:str = Par défaut en noir, la couleur est définie en chaîne de charactère, la couleur du périmètre du rectangle est en noir.
        couleur_fond:tuple or bool or str=False = La couleur en tuple de la surface du rectangle.
        """
        self.l = longueur
        self.L = largeur
        self.c_c = couleur_contour
        self.c_f = couleur_fond
        self.e = epaisseur
    def draw(self):
        """Dessin du rectangle
        L1 = Trace la longueur du rectangle en utilisant la classe Ligne avec pour attribut la longueur du rectangle, son epaisseur et la couleur du périmètre, en noir par défaut.
        L2 = Trace la largeur du rectangle en utilisant la classe Ligne avec pour attribut la largeur du rectangle, son epaisseur et la couleur du périmètre, en noir par défaut.
        La fonction draw permet de dessiner un rectangle en fonction des attributs de la méthode __init__
        """
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