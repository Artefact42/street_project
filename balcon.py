import turtle as t
from rectangle import Rectangle

class Balcon:
    """La classe Balcon utilise le module turtle et rectangle pour créer un balcon généré aléatoirement pour chaque fenêtre d'un immeuble.
        2 modules:
        __init__ est le module constructeur de la classe Balcon
        draw : ce module permet de dessiner le balcon à l'aide du module Rectangle"""
    def __init__(self):
        """Méthode constructeur
        3 valeurs sont définies par défaut, la longueur, la largeur, et l'épaisseur.
        """
        self.l = 38
        self.L = 30
        self.e = 1
    def draw(self):
        """Méthode dessinage du Balcon
        Dessine la un balcon à l'aide des modules turtle et rectangle en fonction de la longueur, la largeur et l'épaisseur prédéfinie dans la méthode __init__
        """
        Rectangle(self.l, self.L, self.e).draw()
        for i in range(10):
            Rectangle(self.l/10, self.L, self.e/2).draw()
            t.backward(self.l/10)