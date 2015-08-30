__author__ = 'brapastor'

class perro:
    tipo = 'canino'  # variable de clse compartida por todas las instancias

    def __init__(self,nombre):
        self.nombre = nombre   # variable de instancia unica para la instancia


d = perro('fido')
e = perro('Chop')

d.tipo               # compartida por todos los perros
print(d.tipo)

e.tipo
print(e.tipo)

d.nombre
print(d.nombre)  # unica para d

e.nombre
print(e.nombre)  # unica para e