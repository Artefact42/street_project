import turtle as t
from sol import Sol
from immeuble import Immeuble

class Rue :
    """Classe Rue utilisant le module turtle, sol, immeuble possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le Rue
    """
    def __init__(self) :
        """Méthode constructeur
        prend aucun paramètres, les attributs self.ox et self.oy sont les origines et sont prédéfinies.
        """
        self.ox = -355
        self.oy = -160 
    def draw (self):
        """Méthode dessinage de la rue
        Dessine à l'aide des modules turtle, sol et un étage en fonction des attributs de la méthode __init__
        """
        t.penup()
        t.goto(self.ox, self.oy)
        t.pendown()
        Sol().draw()
        t.penup()
        t.goto(self.ox, self.oy)
        for i in range(4):
            self.ox +=170
            t.penup()
            t.goto(self.ox, self.oy+60)
            t.pendown()
            Immeuble().draw()