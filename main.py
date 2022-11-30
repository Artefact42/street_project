import turtle as t
from rectangle import Rectangle
from demi_cercle import Demi_cercle
from porte import Porte
from vitre import Vitre

try:
    t.reset()  
except t.Terminator:
    pass

t.hideturtle()
t.speed(10)

t.title("STREET !")
t.setup(640, 480, 100, 100)

"""
Rectangle(200,100,5).draw()

Demi_cercle(rect.l,5).draw()

Porte().draw()
"""

Vitre().draw()

t.exitonclick()