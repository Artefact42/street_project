import turtle as t
from rectangle import Rectangle

class Balcon:
    def __init__(self):
        self.l = 42
        self.L = 30
        self.e = 3
    def draw(self):
        Rectangle(self.l, self.L, self.e).draw()
        for i in range(10):
            Rectangle(self.l/10, self.L, self.e/2.5).draw()
            t.backward(self.l/10)