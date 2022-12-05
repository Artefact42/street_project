import turtle as t
from ligne import Ligne

class rectangle : 
    def __init__(self,longueur:int,epaisseur:int,couleur:str="black"):
        self.l = longueur 
        self.e = epaisseur 
        self.c = couleur 
    def draw(self):
        L = Ligne(self.l,self.e,self.c)
        L.draw()
