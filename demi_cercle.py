import turtle as t

class Demi_cercle :
    """Classe Demi_Cercle utilisant le module turtle, possédant 2 méthodes:
    __init__ = méthode constructeur de la Classe
    draw = méthode pour dessiner le Demi-Cercle
    """
    def __init__(self, diametre:int, epaisseur:int, couleur_contour:str="black", couleur_fond:tuple or bool or str=False):
        """Methode constructeur

        diametre:int = Longueur en entier naturel de la ligne.
        epaisseur:int = Epaisseur en entier naturel de la ligne.
        couleur_contour:str = Par défaut en noir, c'est la couleur de l'épaisseur du demi-cercle
        """
        self.d = diametre
        self.e = epaisseur
        self.c_c = couleur_contour
        self.c_f = couleur_fond
    def draw(self):
        """Méthode dessinage du demi-cercle
        Dessine à l'aide des modules turtle un demi-cercle en fonction des paramètres de la méthode __init__
        """
        if self.c_f != False :
            t.fillcolor(self.c_f)
            t.begin_fill()
        t.pencolor(self.c_c)
        t.pensize(self.e)
        t.circle(self.d/2,180)
        if self.c_f != False :
            t.end_fill()