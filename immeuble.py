import turtle as t
from etage import Etage
from toit import Toit
from random import randint

class Immeuble:
    def __init__ (self) :
        self.c1 = randint(0,255)
        self.c2 = randint(0,255)
        self.c3 = randint(0,255)
        self.nb = randint (0,2)
        self.toit = randint(0,1)

    def draw(self):
        origine = t.pos()
        Etage((self.c1,self.c2,self.c3),True).draw()
        for i in range(self.nb):
            t.goto(origine[0],origine[1]+(60))
            origine = t.pos()
            Etage((self.c1,self.c2,self.c3),False).draw()
        if self.toit == 1 :
            t.goto(origine)
            Toit().draw()