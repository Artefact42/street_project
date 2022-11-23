import turtle as t
from ligne import Ligne
from rectangle import Rectangle

try:
    t.reset()  
except t.Terminator:
    pass

t.title("Ma super fenêtre")
t.setup(640, 480, 100, 100)

rect = Rectangle(200,100,5)
rect.draw()
t.exitonclick()