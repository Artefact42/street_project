import turtle as t
from rue import Rue

try:
    t.reset()  
except t.Terminator:
    pass

t.hideturtle()
t.colormode(255)
t.speed("fastest")
t.title("Street_project Alexis Dorian Gabriel")
t.setup(770, 480)

Rue().draw()

t.exitonclick()