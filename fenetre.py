import turtle as t
from vitre import Vitre
from balcon import Balcon
from random import randint

class Fenetre :
    def __init__(self):
        self.type = randint(1,2)
    def draw(self):
        if self.type == 1 :
            Vitre().draw()
        else :
            v=Vitre()
            b=Balcon()
            v.draw()
            t.penup()
            t.forward((b.l-v.cote)/2)
            t.setheading(270)
            t.forward(b.L-15)
            t.pendown()
            b.draw()