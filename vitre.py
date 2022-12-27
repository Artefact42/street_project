from rectangle import Rectangle

class Vitre :
    """Classe vitre utilisant le module rectangle, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner la vitre
    """
    def __init__(self):
        """Méthode constructeur
        prend aucun paramètres, 
        L'attribut self.e correspond à l'épaisseur de la vitre prédéfinie
        L'attribut self.cote correspond à la longueur de la vitre prédéfinie
        """
        self.e = 1
        self.cote = 30
    def draw(self):
        """Méthode dessinage de la vitre
        Dessine à l'aide du module rectangle. Une vitre en fonction des attributs de la méthode __init__
        """
        Rectangle(self.cote, self.cote, self.e, couleur_fond="cyan").draw()