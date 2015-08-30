from builtins import print

__author__ = 'brapastor'

class Complejo:
    def __init__(self, partereal, parteimaginaria):
        self.r =partereal
        self.i = parteimaginaria

x = Complejo(3.0,-4.5)
x.contador = 1
while x.contador<10:
    x.contador = x.contador*2

print(x.contador)
del x.contador

