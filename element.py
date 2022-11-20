from turtle import *

class Ligne :
    def __init__(self,longeur:int,largeur:int,angle:float,origine:tuple,couleur:str):
        self.l = longeur
        self.L = largeur
        self.a = angle
        self.O = origine
        self.c = couleur
    def draw(self):
        if turtle.isdown() : turtle.penup()
        turle.setposition(self.O[0], self.O[1])
        turtle.setheading(self.a)
        turtle.pencolor(self.c)
        turtle.pensize(self.L)
        turtle.pendown()
        turtle.forward(self.l)
        turtle.penup()

class arc_cercle :
    def __init__(self):
        pass
    def draw(self):
        pass