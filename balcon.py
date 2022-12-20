import turtle as t
from rectangle import Rectangle

class Balcon:
    def __init__(self):
        self.l = 38
        self.L = 30
        self.e = 1
    def draw(self):
        Rectangle(self.l, self.L, self.e).draw()
        for i in range(10):
            Rectangle(self.l/10, self.L, self.e/2).draw()
            t.backward(self.l/10)