from random import randint
from demi_cercle import Demi_cercle
import turtle as t
from triangle import Triangle

class Toit:
    """Classe Toit utilisant le module random, demi_cercle, turtle et triangle, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le toit
    """
    def __init__(self):
        """Methode constructeur
        Prend aucun paramètres : il est composé des 6 attributs suivants:
        self.type = choisi une valeur aléatoire entre 1 et 2
        self.e = définie par défaut, l'attribut correspond à l'epaisseur du toit
        self.l = définie par défaut, l'attribut correspond à la longueur du toit
        self.c = définie par défaut, l'attribut correspond à la couleur du toit en string
        self.angle = définie par défaut, l'attribut correspond à l'angle du toit en degrée
        self.nb_ronds = définie par défaut, l'attribut correpond au nombre de tuiles
        """
        self.type = randint(1,2)
        self.e = 2
        self.l = 140
        self.c = "brown"
        self.angle = 45
        self.nb_ronds = 5
    def draw(self):
        """Méthode dessinage du toit
        Dessine à l'aide des modules random, demi_cercle, turtle et triangle. Un sol en fonction des attributs de la méthode __init__
        """
        if self.type == 1:
            Triangle(self.l, self.angle, self.e, couleur_fond=self.c).draw()
        elif self.type == 2:
            for i in range(self.nb_ronds):
                t.setheading(90)
                Demi_cercle(self.l/self.nb_ronds, self.e, couleur_fond=self.c).draw()