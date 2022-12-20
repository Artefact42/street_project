import turtle as t

class Demi_cercle :
    def __init__(self, diametre:int, epaisseur:int, couleur_contour:str="black", couleur_fond:tuple or bool or str=False):
        self.d = diametre
        self.e = epaisseur
        self.c_c = couleur_contour
        self.c_f = couleur_fond
    def draw(self):
        if self.c_f != False :
            t.fillcolor(self.c_f)
            t.begin_fill()
        t.pencolor(self.c_c)
        t.pensize(self.e)
        t.circle(self.d/2,180)
        if self.c_f != False :
            t.end_fill()