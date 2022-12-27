import turtle as t
from vitre import Vitre
from balcon import Balcon
from random import randint

class Fenetre :
    """Classe Fenetre utilisant le module turtle,vitre, balcon et random, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner la fenetre
    """
    def __init__(self):
        """Méthode constructeur
        1 Attribut : self.type qui génère un nombre aléatoire compris entre 1 et 2.
        """
        self.type = randint(1,2)
    def draw(self):
        """Méthode dessinage de la Fenetre
        Dessine à l'aide des modules turtle, vitre, balcon et random une fenetre celle-ci peut posseder un balcon si :
        le self.type = 2.
        Sinon, la vitre ne possède pas de balcon :
        self.type = 1.
        """
        if self.type == 1 :
            Vitre().draw()
        else :
            v=Vitre()
            b=Balcon()
            v.draw()
            t.penup()
            t.forward((b.l-v.cote)/2)
            t.setheading(270)
            t.forward(b.L-15)
            t.pendown()
            b.draw()