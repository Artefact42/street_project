from turtle import *
from ligne import Ligne

try:
    reset()  
except Terminator:
    pass

title("Ma super fenêtre")
setup(640, 480, 100, 100)

t1 = Ligne(200,42,69,(3,6),"yellow")
t1.draw()

exitonclick()