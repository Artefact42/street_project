import turtle as t

class Demi_cercle :
    def __init__(self, diametre:int, epaisseur:int, couleur:str="black"):
        self.d = diametre
        self.e = epaisseur
        self.c = couleur
    def draw(self):
        t.setheading(90)
        t.pencolor(self.c)
        t.pensize(self.e)
        t.circle(self.d/2,180)