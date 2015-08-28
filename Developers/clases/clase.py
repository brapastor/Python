from builtins import print

__author__ = 'brapastor'

class MiClase:
    """SIMPLE CLASE DE EJEMPLO"""
    i= 12345

    def __init__(self): # UN CONSTRUCTOR
        self.datos=[]

    def f(self):
        return "hola mundo"

x = MiClase()  # INSTANCIACION DE LA CLASE
print(x)
