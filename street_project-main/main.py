import turtle as t
from ligne import Ligne
from rectangle import Rectangle
from demi_cercle import Demi_cercle
from porte import Porte
from vitre import Vitre
from balcon import Balcon
from vitre import Vitre
from fenetre import Fenetre
from toit import Toit
from sol import Sol
from rue import Rue
from etage import Etage



try:
    t.reset()  
except t.Terminator:
    pass

t.hideturtle()
t.colormode(255)
t.speed("fastest")

t.title("Street_project Alexis Dorian Gabriel")
t.setup(770, 480)

"""
Ligne(10,3).draw()
Rectangle(200,100,3).draw()
Demi_cercle(rect.l,3).draw()
Porte().draw()
Vitre().draw()
Balcon().draw()
Fenetre().draw()
Toit().draw()
Rue().draw()
"""
Etage((55,12,6),True).draw()


t.exitonclick()
