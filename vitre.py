import turtle as t
from rectangle import Rectangle

class Vitre :
    def __init__(self):
        self.e = 1
        self.cote = 30
    def draw(self):
        Rectangle(self.cote, self.cote, self.e, couleur_fond="cyan").draw()