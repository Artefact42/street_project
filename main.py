import turtle as t
from rectangle import Rectangle
from demi_cercle import Demi_cercle

try:
    t.reset()  
except t.Terminator:
    pass

t.title("Ma super fenêtre")
t.setup(640, 480, 100, 100)

rect = Rectangle(200,100,5)
rect.draw()

cer = Demi_cercle(rect.l,7)
cer.draw()

t.exitonclick()