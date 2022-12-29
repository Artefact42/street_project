import turtle as t
from etage import Etage
from toit import Toit
from random import randint

class Immeuble:
    """Classe Fenetre utilisant le module étage, toit, et random, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner l'immeuble
    """
    def __init__ (self) :
        """Méthode constructeur
        prend aucun paramètres, 
        Les attributs self.r, self.v et self.b correspondent à rouge vert et bleu pour la couleur aléatoire de l'immeuble.
        l'attribut self.nb définie la taille de l'immeuble
        """
        self.r = randint(0,255)
        self.v = randint(0,255)
        self.b = randint(0,255)
        self.nb = randint (0,4)

    def draw(self):
        """Méthode dessinage de l'Etage
        Dessine à l'aide du module turtle, etage, toit et random un immeuble en fonction des attributs de la méthode __init__
        """
        origine = t.pos()
        Etage((self.r,self.v,self.b),True).draw()
        for i in range(self.nb):
            t.goto(origine[0],origine[1]+(60))
            origine = t.pos()
            t.pendown()
            Etage((self.r,self.v,self.b),False).draw()
        t.goto(origine)
        t.pendown()
        Toit().draw()