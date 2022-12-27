import turtle as t

class Ligne :
    """Classe Python permettant de créer une ligne à l'aide du module turtle.
    
    """
    def __init__(self,longeur:int,epaisseur:int,couleur:str="black"):
        """Methode constructeur

        longueur:int = Longueur en entier naturel de la ligne.
        epaisseur:int = Epaisseur en entier naturel de la ligne.
        couleur:str = Par défaut en noir, la couleur est définie en chaîne de charactère.

        """
        self.l = longeur
        self.e = epaisseur
        self.c = couleur
    def draw(self):
        """Permet de tracer une ligne en fonction des attributs de la méthode __init__
        """
        t.pencolor(self.c)
        t.pensize(self.e)
        t.forward(self.l)