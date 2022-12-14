import turtle as t

class Ligne :
    def __init__(self,longeur:int,epaisseur:int,couleur:str="black"):
        self.l = longeur
        self.e = epaisseur
        self.c = couleur
    def draw(self):
        t.pencolor(self.c)
        t.pensize(self.e)
        t.forward(self.l)