from ligne import Ligne

class Sol : 
    def __init__(self):
        self.l = 710 
        self.e = 4 
        self.c = "grey" 
    def draw(self):
        L = Ligne(self.l,self.e,self.c)
        L.draw()