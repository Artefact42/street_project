import turtle as t
from ligne import Ligne
from rectangle import Rectangle
from demi_cercle import Demi_cercle
from porte import Porte
from vitre import Vitre
from balcon import Balcon
from vitre import Vitre
from fenetre import Fenetre

try:
    t.reset()  
except t.Terminator:
    pass

t.hideturtle()
t.speed(10)

t.title("STREET !")
t.setup(640, 480, 100, 100)

"""
Ligne(10,3).draw()
Rectangle(200,100,3).draw()
Demi_cercle(rect.l,3).draw()
Porte().draw()
Vitre().draw()
Balcon().draw()
Vitre().draw()
"""

Fenetre().draw()

t.exitonclick()