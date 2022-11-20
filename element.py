from turtle import *

class Ligne :
    def __init__(self,longeur:int,largeur:int,angle:float,origine:tuple,couleur:str):
        self.l = longeur
        self.L = largeur
        self.a = angle
        self.O = origine
        self.c = couleur
    def draw(self):
        if isdown() : penup()
        setposition(self.O[0], self.O[1])
        setheading(self.a)
        pencolor(self.c)
        pensize(self.L)
        pendown()
        forward(self.l)
        penup()

class arc_cercle :
    def __init__(self):
        pass
    def draw(self):
        pass