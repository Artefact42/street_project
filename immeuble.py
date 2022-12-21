import turtle as t
from etage import Etage
from toit import Toit
from random import randint

class Immeuble:
    def __init__ (self) :
        self.r = randint(0,255)
        self.v = randint(0,255)
        self.b = randint(0,255)
        self.nb = randint (0,3)

    def draw(self):
        origine = t.pos()
        Etage((self.r,self.v,self.b),True).draw()
        for i in range(self.nb):
            t.goto(origine[0],origine[1]+(60))
            origine = t.pos()
            t.pendown()
            Etage((self.r,self.v,self.b),False).draw()
        t.goto(origine)
        t.pendown()
        Toit().draw()