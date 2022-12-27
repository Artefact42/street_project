import turtle as t
from random import randint
from rectangle import Rectangle
from porte import Porte
from fenetre import Fenetre

class Etage:
    """Classe Etage utilisant le module turtle, random, rectangle, porte et fenetre possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner l'étage de l'immeuble avec pour objet, la porte et la fenetre 
    """
    def __init__(self, couleur:tuple, rdc:bool):
        """Méthode constructeur
        prend 2 paramètres, la couleur en tuple et un booléen indiquant si l'étage est un rez-de-chaussée ou non.
        Les attributs l'hauteur, la longueur, la largeur et l'épaisseur sont prédéfinies.
        """
        self.h = 60
        self.L = 140
        self.e = 1
        self.c = couleur
        self.rdc = rdc
    def draw(self):
        """Méthode dessinage de l'Etage
        Dessine à l'aide des modules turtle, rectangle, fenetre et porte un étage en fonction des paramètres de la méthode __init__
        """
        origine = t.pos()
        if self.rdc :
            position_porte = randint(0,2)
            Rectangle(self.L,self.h,self.e,couleur_fond=self.c).draw()
            t.penup()
            for i in range (3):
                if i == position_porte :
                    p = Porte()
                    if p.type == 1 :
                        t.goto(origine[0]-(15+i*40),origine[1]-self.h+p.L)
                        t.pendown()
                        p.draw()
                    else:
                        t.goto(origine[0]-(15+i*40+p.l),origine[1]-self.h+p.L-p.diminution_porte2)
                        t.pendown()
                        p.draw()
                    t.penup()
                else :
                    t.goto(origine[0]-(15+i*40),origine[1]-8)
                    t.pendown()
                    Fenetre().draw()
                    t.penup()
        else :
            Rectangle(self.L,self.h,self.e,couleur_fond=self.c).draw()
            t.penup()
            for i in range(3):
                t.goto(origine[0]-(15+i*40),origine[1]-8)
                t.pendown()
                Fenetre().draw()
                t.penup()