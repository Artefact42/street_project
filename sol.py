from ligne import Ligne

class Sol : 
    """Classe Sol utilisant le module ligne possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le sol
    """
    def __init__(self):
        """Methode constructeur
        Prend aucun paramètres, les attributs longueur, epaisseur et couleur sont prédéfinies.
        """
        self.l = 710 
        self.e = 4 
        self.c = "grey" 
    def draw(self):
        """Méthode dessinage du sol
        Dessine à l'aide du module ligne un sol en fonction des attributs de la méthode __init__
        """
        L = Ligne(self.l,self.e,self.c)
        L.draw()